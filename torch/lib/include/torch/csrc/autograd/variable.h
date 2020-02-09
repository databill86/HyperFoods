#pragma once

#include "torch/csrc/utils/python_stub.h"

#include "torch/csrc/assertions.h"
#include "torch/csrc/autograd/edge.h"
#include "torch/csrc/autograd/function_hook.h"
#include "torch/csrc/autograd/variable_version.h"
#include "torch/csrc/utils/auto_unique_ptr.h"

#include <ATen/ATen.h>
#include <ATen/Error.h>

#include <list>
#include <memory>
#include <mutex>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace torch {
namespace autograd {
struct Function;
} // namespace autograd
namespace jit { namespace tracer {
// Has to be forward declared because tracer_state.h has a dependency on
// variable.h.
struct ValueTracingStateElem;
using ValueTracingState = std::list<ValueTracingStateElem>;
}} // namespace jit::tracer
} // namespace torch

namespace torch { namespace autograd {

///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
///                                Variable
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/// A `Variable` augments a `Tensor` with the ability to interact in our
/// autograd machinery. Conceptually, `Variable`s travel along `Edge`s between
/// `Function`s in the autograd graph. A `Variable` can either be a leaf, like a
/// weight in a neural network, or an interior variable, when it is the result
/// of an operation between variables. Every `Variable` also stores another
/// `Variable` called its `grad` (gradient). If the variable is a leaf, its
/// gradient will be accumulated into this variable.
///
///                              Gradient Edges
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/// Furthermore, `Variable`s have the notion of a `gradient_edge`, which is the
/// edge in the autograd graph that connects the variable to a particular input
/// of the gradient function that will be invoked with the variable during the
/// backward pass. More precisely, this gradient function can be one of two
/// things:
/// 1. A `grad_fn`, if the variable is in the interior of the graph. This is the
///    gradient of the function that produced the variable.
/// 2. A `grad_accumulator`, if the variable is a leaf, which accumulates a
///    scalar gradient value into its `grad` variable.
///
///                               Versioning
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/// Another major feature of `Variable`s are *versions*. Versions are
/// incremented when an in-place mutation of a variable occurs. Versions are
/// useful when constructing `SavedVariable`s, which take a snapshot of a
/// `Variable` at a certain version. You can retrieve a `Variable`'s version
/// through its `current_version()` method.
///
///                                 Views
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/// It is possible for a  `Variable` to be a *view* of another `Variable`, in
/// which case it tracks that `Variable`'s data and autograd history. Beyond
/// construction, the interface of a view is identical to that of a regular
/// `Variable`. You can determine whether `Variable` is in fact a view by
/// probing its `is_view()` method.
///
///                               Interface
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/// `Variable` inherits from `Tensor` and thus its API is a superset of that of
/// `Tensor`. This means you can perform all the usual mathematical and other
/// operations you can perform on `Tensor`s also on `Variable`s. Furthermore,
/// `Variable` and `Tensor` actually convert implicitly between each other. You
/// can thus call functions defined on `Tensor`s also with `Variable`s. For
/// this, the `Variable` class allows implicit construction from `Tensor`. It is
/// the responsibility of calling code to ensure that this constructor is
/// invoked only when the `Tensor`'s dynamic type is actually `Variable`. Most
/// notably, it is *not* correct to construct a brand new `Variable` from a
/// `Tensor` using this constructor. To do so, you must use the `make_variable`
/// free function instead. To create a view variable, use `make_variable_view`.
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

struct Variable : public at::Tensor {
  /// Default constructor.
  Variable() = default;

  // Factory Functions
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  // NOTE: These factory functions have to be friends to access the
  // `Variable::Impl`. As a side effect, it allows us to keep them in the class.

  /// Creates a `Variable` that is a *view* of another (*base*) variable.
  /// The `gradient_edge` is an optional (gradient_function, input_number) pair.
  friend Variable make_variable_view(
      Variable base,
      at::Tensor data,
      Edge gradient_edge);

  /// Creates a `Variable` from the given `Tensor`. `requires_grad` should be
  /// set only for leaves, and determines whether the `Variable` will accumulate
  /// gradients. NOTE: `data` must *not* be a `Variable` already. Its dynamic
  /// type *must* be `Tensor`.
  friend Variable make_variable(at::Tensor data, bool requires_grad);

  /// Creates a `Variable` from the given `Tensor` and specify a
  /// `gradient_edge`, i.e. a (function, input_nr) pair specifying the function
  /// in the autograd graph, and what particular input of that function, this
  /// variable is connected to.
  friend Variable make_variable(at::Tensor data, Edge gradient_edge);

  // Tensor Conversions
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  // "Downcasts" a `Tensor` into a `Variable`. Only call this on tensors you
  // know are Variables.
  /*implicit*/ Variable(at::Tensor const& rhs) : at::Tensor(rhs) {
    TORCH_ASSERTM(
        is_variable() || !defined(),
        "Tensor that was converted to Variable was not actually a Variable");
  }

  /*implicit*/ Variable(at::Tensor&& rhs) noexcept
      : at::Tensor(std::move(rhs)) {
    TORCH_ASSERTM(
        is_variable() || !defined(),
        "Tensor that was converted to Variable was not actually a Variable");
  }

  // NOTE: Assignment operators to Tensor come for free from the constructors.

  const at::Tensor& data() const noexcept;
  at::Tensor& data() noexcept;

  // Gradient Function and Edges
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  /// Gets the gradient function of the `Variable`. If this is a leaf variable,
  /// the pointer returned will be null.
  const std::shared_ptr<Function>& grad_fn() const;

  /// Gets the raw gradient function pointer, whatever it currently is.
  Function* grad_fn_unsafe() const;

  /// Set the gradient accumulator of the `Variable`. This is only applicable to
  /// leaf variables. Interior variables should call `set_gradient_edge()`.
  void set_grad_accumulator(std::weak_ptr<Function> grad_accumulator);

  /// Attempts to get a pointer to the gradient accumulator of the `Variable`,
  /// if it still exists. If the gradient accumulator function has been
  /// destroyed, returns a `nullptr`.
  std::shared_ptr<Function> try_get_grad_accumulator() const;

  /// Gets the gradient accumulator of the `Variable` if it has one, or else
  /// create one on the fly and return it.
  std::shared_ptr<Function> grad_accumulator() const;

  /// Returns the "canonical" gradient edge of this `Variable`, i.e. either the
  /// gradient function if this is an interior `Variable`, or the gradient
  /// accumulator otherwise. If the `Variable` is interior, the returned `Edge`
  /// will store the input index of the `Function` to which this variable is
  /// connected in its `input_nr` field. For leaves, the `input_nr` is always
  /// zero. Note that `set_gradient_edge` and `gradient_edge` are not
  /// symmetric. You must use `set_gradient_edge` to set the `grad_fn` and
  /// `set_grad_accumulator` to set the accumulator.
  Edge gradient_edge() const {
    // If grad_fn is null (as is the case for a leaf node), we instead
    // interpret the gradient function to be a gradient accumulator, which will
    // accumulate its inputs into the grad property of the variable. These
    // nodes get suppressed in some situations, see "suppress gradient
    // accumulation" below. Note that only variables which have `requires_grad =
    // True` can have gradient accumulators.
    if (const auto& gradient = grad_fn()) {
      return Edge(gradient, output_nr());
    } else {
      return Edge(grad_accumulator(), 0);
    }
  }

  /// Set the gradient edge -- i.e. `grad_fn` and `input_nr` -- of the
  /// `Variable`.
  /// NOTE: This will always set the `grad_fn`, even if this is a leaf variable,
  /// and never the `grad_accumulator`. For the latter, use
  /// `set_grad_accumulator`. This allows late construction of an interior
  /// `Variable`.
  void set_gradient_edge(Edge edge) noexcept;

  /// Returns the input index of the gradient `Function` to which this
  /// `Variable` is connected.
  uint32_t output_nr() const noexcept;

  /// True if this `Variable` is a leaf and thus does not have a `grad_fn`.
  bool is_leaf() const noexcept;

  // Versions
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  /// Increments the version count of this `Variable`.
  void bump_version() noexcept;
  void set_version_counter(const VariableVersion& version_counter) noexcept;

  /// Retrieves this `Variable`s version counter.
  const VariableVersion& version_counter() const noexcept;

  /// Retrieves the current value of the `Variable`'s version counter.
  /// Equivalent to calling `version_counter().current_version()`.
  uint32_t current_version() const noexcept;

  // Autograd Graph Interaction
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  /// Update the `grad_fn` of an existing Variable. Called after in-place
  /// modifications.
  void rebase_history(Edge gradient_edge);

  // Hooks
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  void add_hook(std::shared_ptr<FunctionPreHook> hook);
  const std::vector<std::shared_ptr<FunctionPreHook>>& hooks() const noexcept;
  void clear_hooks();

  // JIT Tracing
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  void set_tracing_state(jit::tracer::ValueTracingState* new_tracing_state);
  jit::tracer::ValueTracingState& tracing_state() const noexcept;

  /// Returns true if the `Variable`'s tracing state is not null.
  bool has_tracing_state() const noexcept;

  // View Variables
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  /// Returns true if this `Variable` is a view of another `Variable`.
  bool is_view() const noexcept;

  /// Returns the `Variable` that this `Variable` is a view of. If this
  /// `Variable` is not a view, throw a `std::runtime_error`.
  const Variable& base() const;

  // Miscellaneous
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  /// Compares this `Variable` to another `Variable` (or `Tensor`) via
  /// pointer-equality.
  bool is_same(const Variable& other) const noexcept {
    return this->pImpl == other.pImpl;
  }

  void set_name(const std::string& name);
  const std::string& name() const noexcept;

  PyObject* pyobj() const noexcept;
  void set_pyobj(PyObject* pyobj) noexcept;

 private:
  /// Private implementation struct of the `Variable`. This struct declaration
  /// and the `get()` method which exposes it shall forever remain private and
  /// never be exposed to the public interface of this class.
  struct Impl;
  struct ViewImpl;

  // Private Methods
  //~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Variable(Variable::Impl* self, bool retain);
  Impl* get() const noexcept;
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//                            Variable::Impl
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

struct Variable::Impl : public at::TensorImpl {
  explicit Impl(
      at::Tensor data,
      bool requires_grad = false,
      Edge edge = Edge());

  ~Impl() override;

  const char* toString() const override;
  at::IntList sizes() const override;
  at::IntList strides() const override;
  int64_t dim() const override;
  at::Scalar localScalar() override;
  void* unsafeGetTH(bool retain) override;
  std::unique_ptr<at::Storage> storage() override;
  static const char* typeString();

  std::shared_ptr<Function> get_grad_accumulator();
  virtual std::shared_ptr<Function>& get_grad_fn() {
    return grad_fn_;
  }

  virtual const Variable& base() const {
    throw std::runtime_error("Can't get base of non-view Variable");
  }

  /// Sets the `requires_grad` property of `Variable`. This should be true for
  /// leaf variables that want to accumulate gradients, and false for all other
  /// variables.
  void set_requires_grad(bool requires_grad) override {
    AT_CHECK(
        !requires_grad || at::isFloatingType(type().scalarType()),
        "Only Tensors of floating point dtype can require gradients");
    requires_grad_ = requires_grad;
  }

  bool requires_grad() const override {
    return requires_grad_ || grad_fn_ || (is_view_ && base().requires_grad());
  }

  /// Accesses the gradient `Variable` of this `Variable`.
  Tensor& grad() override {
    return grad_;
  }
  const Variable& grad() const override {
    return grad_;
  }

  /// Returns a copy of this `Variable` that is detached from its autograd graph
  /// and has a blank version. This method is OK to call if the `Variable` is a
  /// view.
  Tensor detach() const override;

  /// Like `detach()`, but removes this `Variable` in-place. This method may
  /// only be called on non-view `Variable`s. You can use `is_view()` to check
  /// this. If this `Variable` is a view, throws an `std::runtime_error()`.
  void detach_() override;

  /// Sets the type of the Variable.
  void set_data(Tensor new_data) override;

  /// Computes the gradient of current tensor w.r.t. graph leaves.
  void backward(
      at::optional<at::Tensor> gradient,
      bool keep_graph,
      bool create_graph) override;

  /// Reset all expensive fields to free up resources
  void release_resources() override;

  // Make this field public so we can access it from `Variable`.
  using at::TensorImpl::type_;

  std::string name;
  at::Tensor data_;

  Variable grad_;
  std::shared_ptr<Function> grad_fn_;
  std::weak_ptr<Function> grad_accumulator_;

  VariableVersion version_counter_;
  std::vector<std::shared_ptr<FunctionPreHook>> hooks_;

  // Only meaningful on leaf variables (must be false otherwise)
  bool requires_grad_;

  bool is_view_;

  // The "output number" of this variable; e.g., if this variable
  // was the second output of a function, then output_nr == 1.
  // We use this to make sure we can setup the backwards trace
  // correctly when this variable is passed to another function.
  uint32_t output_nr_;
  PyObject* pyobj_; // weak reference

  // Mutex to ensure that concurrent read operations that modify internal
  // state are still thread-safe. Used by get_grad_fn and
  // get_grad_accumulator.
  std::mutex mutex_;

  // For use in torch::jit::tracer
  auto_unique_ptr<jit::tracer::ValueTracingState> tracing_state_;
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//                          Variable::ViewImpl
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/// A Variable that is a view on another Variable. The base and view share the
/// same version_counter. The grad_fn field of the Variable may become stale
/// due to in-place modifications of the shared data. Accesses should go
/// through get_grad_fn(). All other fields are always valid.
struct Variable::ViewImpl : public Variable::Impl {
  ViewImpl(Variable base, at::Tensor data, Edge gradient_edge);

  /// Gets the up-to-date grad_fn. If the shared data or base was modified, we
  /// re-create the grad_fn to express the up-to-date view relationship between
  /// this and the base Variable.
  std::shared_ptr<Function>& get_grad_fn() override;

  const Variable& base() const override {
    return base_;
  }

  /// Reset all expensive fields to free up resources
  void release_resources() override;

  /// Called after in-place modifications. Modifies the grad_fn of the base
  /// Variable.
  void rebase_history(Edge gradient_edge);

  /// The base `Variable` (never a view).
  Variable base_;

  /// The value of the version_counter at the time grad_fn was created. The
  /// grad_fn field is stale if attr_version !=
  /// version_counter.current_version().
  uint32_t attr_version;
};

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//                        Variable Implementation
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// Factory Functions
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline Variable make_variable_view(
    Variable base,
    at::Tensor data,
    Edge gradient_edge = Edge()) {
  if (data.defined()) {
    auto impl = new Variable::ViewImpl(
        std::move(base), std::move(data), std::move(gradient_edge));
    return Variable(impl, /*retain=*/false);
  }
  return Variable();
}

inline Variable make_variable(at::Tensor data, bool requires_grad = false) {
  AT_CHECK(
      !data.is_variable(),
      "Must not create a new variable from a variable, use its .data()");
  if (data.defined()) {
    auto impl = new Variable::Impl(data, requires_grad);
    return Variable(impl, /*retain=*/false);
  }
  return Variable();
}

inline Variable make_variable(at::Tensor data, Edge gradient_edge) {
  AT_CHECK(
      !data.is_variable(),
      "Must not create a new variable from a variable, use its .data()");
  if (data.defined()) {
    auto impl = new Variable::Impl(data, false, std::move(gradient_edge));
    return Variable(impl, /*retain=*/false);
  }
  return Variable();
}

// Tensor Conversion
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

/// Downcasts the `Tensor` reference to a `Variable` reference. If compiling
/// in DEBUG mode and the tensor's dynamic type is not in fact `Variable`,
/// throws a `std::invalid_argument` exception.
inline Variable& as_variable_ref(at::Tensor& tensor) {
  AT_CHECK(
      tensor.is_variable(),
      "Attempted to cast a Tensor to a Variable, but "
      "the dynamic type of the value is not Variable.");
  return static_cast<Variable&>(tensor);
}

inline const Variable& as_variable_ref(const at::Tensor& tensor) {
  AT_CHECK(
      tensor.is_variable(),
      "Attempted to cast a Tensor to a Variable, but "
      "the dynamic type of the value is not Variable.");
  return static_cast<const Variable&>(tensor);
}

inline const at::Tensor& Variable::data() const noexcept {
  return get()->data_;
}

inline at::Tensor& Variable::data() noexcept {
  return get()->data_;
}

// Gradient Function and Edges
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline const std::shared_ptr<Function>& Variable::grad_fn() const {
  return get()->get_grad_fn();
}

inline Function* Variable::grad_fn_unsafe() const {
  return get()->grad_fn_.get();
}

inline void Variable::set_grad_accumulator(
    std::weak_ptr<Function> grad_accumulator) {
  get()->grad_accumulator_ = std::move(grad_accumulator);
}

inline std::shared_ptr<Function> Variable::try_get_grad_accumulator() const {
  return get()->grad_accumulator_.lock();
}

inline std::shared_ptr<Function> Variable::grad_accumulator() const {
  return get()->get_grad_accumulator();
}

inline void Variable::set_gradient_edge(Edge edge) noexcept {
  get()->grad_fn_ = std::move(edge.function);
  get()->output_nr_ = edge.input_nr;
}

inline uint32_t Variable::output_nr() const noexcept {
  return get()->output_nr_;
}

inline bool Variable::is_leaf() const noexcept {
  return get()->grad_fn_ == nullptr;
}

// Versions
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline void Variable::set_version_counter(
    const VariableVersion& version_counter) noexcept {
  get()->version_counter_ = version_counter;
}

inline void Variable::bump_version() noexcept {
  get()->version_counter_.bump();
}

inline uint32_t Variable::current_version() const noexcept {
  return get()->version_counter_.current_version();
}

inline const VariableVersion& Variable::version_counter() const noexcept {
  return get()->version_counter_;
}

// Hooks
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline void Variable::add_hook(std::shared_ptr<FunctionPreHook> hook) {
  get()->hooks_.push_back(std::move(hook));
}

inline const std::vector<std::shared_ptr<FunctionPreHook>>& Variable::hooks()
    const noexcept {
  return get()->hooks_;
}

inline void Variable::clear_hooks() {
  get()->hooks_.clear();
}

// JIT Tracing
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline bool Variable::has_tracing_state() const noexcept {
  return get()->tracing_state_ != nullptr;
}

// View Variables
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline bool Variable::is_view() const noexcept {
  return get()->is_view_;
}

inline const Variable& Variable::base() const {
  return get()->base();
}

// Miscellaneous
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline void Variable::set_name(const std::string& name) {
  get()->name = name;
}

inline const std::string& Variable::name() const noexcept {
  return get()->name;
}

inline void Variable::set_pyobj(PyObject* pyobj) noexcept {
  get()->pyobj_ = pyobj;
}

inline PyObject* Variable::pyobj() const noexcept {
  return get()->pyobj_;
}

// Private Methods
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

inline Variable::Variable(Variable::Impl* self, bool retain)
    : at::Tensor(self, retain) {}

inline Variable::Impl* Variable::get() const noexcept {
  TORCH_ASSERTM(defined(), "Called Variable::get() on an undefined Variable");
  return static_cast<Variable::Impl*>(pImpl);
}
}} // namespace torch::autograd
