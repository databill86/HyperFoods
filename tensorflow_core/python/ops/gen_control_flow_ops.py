"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: control_flow_ops.cc
"""

import collections

from tensorflow.python import pywrap_tensorflow as _pywrap_tensorflow
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export


def abort(error_msg="", exit_without_error=False, name=None):
  r"""Raise a exception to abort the process when called.

  If exit_without_error is true, the process will exit normally,
  otherwise it will exit with a SIGABORT signal.

  Returns nothing but an exception.

  Args:
    error_msg: An optional `string`. Defaults to `""`.
      A string which is the message associated with the exception.
    exit_without_error: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Abort", name,
        tld.op_callbacks, "error_msg", error_msg, "exit_without_error",
        exit_without_error)
      return _result
    except _core._FallbackException:
      try:
        return abort_eager_fallback(
            error_msg=error_msg, exit_without_error=exit_without_error,
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if error_msg is None:
    error_msg = ""
  error_msg = _execute.make_str(error_msg, "error_msg")
  if exit_without_error is None:
    exit_without_error = False
  exit_without_error = _execute.make_bool(exit_without_error, "exit_without_error")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Abort", error_msg=error_msg, exit_without_error=exit_without_error,
                 name=name)
  return _op
Abort = tf_export("raw_ops.Abort")(_ops.to_raw_op(abort))


def abort_eager_fallback(error_msg, exit_without_error, name, ctx):
  if error_msg is None:
    error_msg = ""
  error_msg = _execute.make_str(error_msg, "error_msg")
  if exit_without_error is None:
    exit_without_error = False
  exit_without_error = _execute.make_bool(exit_without_error, "exit_without_error")
  _inputs_flat = []
  _attrs = ("error_msg", error_msg, "exit_without_error", exit_without_error)
  _result = _execute.execute(b"Abort", 0, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  _result = None
  return _result


def control_trigger(name=None):
  r"""Does nothing. Serves as a control trigger for scheduling.

  Only useful as a placeholder for control edges.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "ControlTrigger", name,
        tld.op_callbacks)
      return _result
    except _core._FallbackException:
      try:
        return control_trigger_eager_fallback(
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "ControlTrigger", name=name)
  return _op
ControlTrigger = tf_export("raw_ops.ControlTrigger")(_ops.to_raw_op(control_trigger))


def control_trigger_eager_fallback(name, ctx):
  _inputs_flat = []
  _attrs = None
  _result = _execute.execute(b"ControlTrigger", 0, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  _result = None
  return _result


def enter(data, frame_name, is_constant=False, parallel_iterations=10, name=None):
  r"""Creates or finds a child frame, and makes `data` available to the child frame.

  This op is used together with `Exit` to create loops in the graph.
  The unique `frame_name` is used by the `Executor` to identify frames. If
  `is_constant` is true, `output` is a constant in the child frame; otherwise
  it may be changed in the child frame. At most `parallel_iterations` iterations
  are run in parallel in the child frame.

  Args:
    data: A `Tensor`. The tensor to be made available to the child frame.
    frame_name: A `string`. The name of the child frame.
    is_constant: An optional `bool`. Defaults to `False`.
      If true, the output is constant within the child frame.
    parallel_iterations: An optional `int`. Defaults to `10`.
      The number of iterations allowed to run in parallel.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Enter", name,
        tld.op_callbacks, data, "frame_name", frame_name, "is_constant",
        is_constant, "parallel_iterations", parallel_iterations)
      return _result
    except _core._FallbackException:
      try:
        return enter_eager_fallback(
            data, frame_name=frame_name, is_constant=is_constant,
            parallel_iterations=parallel_iterations, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  frame_name = _execute.make_str(frame_name, "frame_name")
  if is_constant is None:
    is_constant = False
  is_constant = _execute.make_bool(is_constant, "is_constant")
  if parallel_iterations is None:
    parallel_iterations = 10
  parallel_iterations = _execute.make_int(parallel_iterations, "parallel_iterations")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Enter", data=data, frame_name=frame_name, is_constant=is_constant,
                 parallel_iterations=parallel_iterations, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "frame_name",
              _op.get_attr("frame_name"), "is_constant",
              _op._get_attr_bool("is_constant"), "parallel_iterations",
              _op._get_attr_int("parallel_iterations"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Enter", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

Enter = tf_export("raw_ops.Enter")(_ops.to_raw_op(enter))


def enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx):
  frame_name = _execute.make_str(frame_name, "frame_name")
  if is_constant is None:
    is_constant = False
  is_constant = _execute.make_bool(is_constant, "is_constant")
  if parallel_iterations is None:
    parallel_iterations = 10
  parallel_iterations = _execute.make_int(parallel_iterations, "parallel_iterations")
  _attr_T, (data,) = _execute.args_to_matching_eager([data], ctx)
  _inputs_flat = [data]
  _attrs = ("T", _attr_T, "frame_name", frame_name, "is_constant",
  is_constant, "parallel_iterations", parallel_iterations)
  _result = _execute.execute(b"Enter", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Enter", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def _exit(data, name=None):
  r"""Exits the current frame to its parent frame.

  Exit makes its input `data` available to the parent frame.

  Args:
    data: A `Tensor`. The tensor to be made available to the parent frame.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Exit", name, tld.op_callbacks,
        data)
      return _result
    except _core._FallbackException:
      try:
        return _exit_eager_fallback(
            data, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Exit", data=data, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Exit", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

Exit = tf_export("raw_ops.Exit")(_ops.to_raw_op(_exit))


def _exit_eager_fallback(data, name, ctx):
  _attr_T, (data,) = _execute.args_to_matching_eager([data], ctx)
  _inputs_flat = [data]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"Exit", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Exit", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def loop_cond(input, name=None):
  r"""Forwards the input to the output.

  This operator represents the loop termination condition used by the
  "pivot" switches of a loop.

  Args:
    input: A `Tensor` of type `bool`.
      A boolean scalar, representing the branch predicate of the Switch op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "LoopCond", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return loop_cond_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "LoopCond", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ()
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "LoopCond", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

LoopCond = tf_export("raw_ops.LoopCond")(_ops.to_raw_op(loop_cond))


def loop_cond_eager_fallback(input, name, ctx):
  input = _ops.convert_to_tensor(input, _dtypes.bool)
  _inputs_flat = [input]
  _attrs = None
  _result = _execute.execute(b"LoopCond", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "LoopCond", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_MergeOutput = collections.namedtuple(
    "Merge",
    ["output", "value_index"])


def merge(inputs, name=None):
  r"""Forwards the value of an available tensor from `inputs` to `output`.

  `Merge` waits for at least one of the tensors in `inputs` to become available.
  It is usually combined with `Switch` to implement branching.

  `Merge` forwards the first tensor to become available to `output`, and sets
  `value_index` to its index in `inputs`.

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type.
      The input tensors, exactly one of which will become available.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, value_index).

    output: A `Tensor`. Has the same type as `inputs`.
    value_index: A `Tensor` of type `int32`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Merge", name,
        tld.op_callbacks, inputs)
      _result = _MergeOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return merge_eager_fallback(
            inputs, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'merge' Op, not %r." % inputs)
  _attr_N = len(inputs)
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Merge", inputs=inputs, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "N", _op._get_attr_int("N"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Merge", _inputs_flat, _attrs, _result)
  _result = _MergeOutput._make(_result)
  return _result

Merge = tf_export("raw_ops.Merge")(_ops.to_raw_op(merge))


def merge_eager_fallback(inputs, name, ctx):
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'merge' Op, not %r." % inputs)
  _attr_N = len(inputs)
  _attr_T, inputs = _execute.args_to_matching_eager(list(inputs), ctx)
  _inputs_flat = list(inputs)
  _attrs = ("T", _attr_T, "N", _attr_N)
  _result = _execute.execute(b"Merge", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Merge", _inputs_flat, _attrs, _result)
  _result = _MergeOutput._make(_result)
  return _result


def next_iteration(data, name=None):
  r"""Makes its input available to the next iteration.

  Args:
    data: A `Tensor`. The tensor to be made available to the next iteration.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "NextIteration", name,
        tld.op_callbacks, data)
      return _result
    except _core._FallbackException:
      try:
        return next_iteration_eager_fallback(
            data, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "NextIteration", data=data, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "NextIteration", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

NextIteration = tf_export("raw_ops.NextIteration")(_ops.to_raw_op(next_iteration))


def next_iteration_eager_fallback(data, name, ctx):
  _attr_T, (data,) = _execute.args_to_matching_eager([data], ctx)
  _inputs_flat = [data]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"NextIteration", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "NextIteration", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('no_op')
def no_op(name=None):
  r"""Does nothing. Only useful as a placeholder for control edges.

  Args:
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "NoOp", name, tld.op_callbacks)
      return _result
    except _core._FallbackException:
      try:
        return no_op_eager_fallback(
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              no_op, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "NoOp", name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          no_op, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  return _op
NoOp = tf_export("raw_ops.NoOp")(_ops.to_raw_op(no_op))


def no_op_eager_fallback(name, ctx):
  _inputs_flat = []
  _attrs = None
  _result = _execute.execute(b"NoOp", 0, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  _result = None
  return _result


def ref_enter(data, frame_name, is_constant=False, parallel_iterations=10, name=None):
  r"""Creates or finds a child frame, and makes `data` available to the child frame.

  The unique `frame_name` is used by the `Executor` to identify frames. If
  `is_constant` is true, `output` is a constant in the child frame; otherwise
  it may be changed in the child frame. At most `parallel_iterations` iterations
  are run in parallel in the child frame.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the child frame.
    frame_name: A `string`. The name of the child frame.
    is_constant: An optional `bool`. Defaults to `False`.
      If true, the output is constant within the child frame.
    parallel_iterations: An optional `int`. Defaults to `10`.
      The number of iterations allowed to run in parallel.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_enter op does not support eager execution. Arg 'output' is a ref.")
  # Add nodes to the TensorFlow graph.
  frame_name = _execute.make_str(frame_name, "frame_name")
  if is_constant is None:
    is_constant = False
  is_constant = _execute.make_bool(is_constant, "is_constant")
  if parallel_iterations is None:
    parallel_iterations = 10
  parallel_iterations = _execute.make_int(parallel_iterations, "parallel_iterations")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefEnter", data=data, frame_name=frame_name, is_constant=is_constant,
                    parallel_iterations=parallel_iterations, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "frame_name",
              _op.get_attr("frame_name"), "is_constant",
              _op._get_attr_bool("is_constant"), "parallel_iterations",
              _op._get_attr_int("parallel_iterations"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefEnter", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RefEnter = tf_export("raw_ops.RefEnter")(_ops.to_raw_op(ref_enter))


def ref_enter_eager_fallback(data, frame_name, is_constant, parallel_iterations, name, ctx):
  raise RuntimeError("ref_enter op does not support eager execution. Arg 'output' is a ref.")

def ref_exit(data, name=None):
  r"""Exits the current frame to its parent frame.

  Exit makes its input `data` available to the parent frame.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the parent frame.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_exit op does not support eager execution. Arg 'output' is a ref.")
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefExit", data=data, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefExit", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RefExit = tf_export("raw_ops.RefExit")(_ops.to_raw_op(ref_exit))


def ref_exit_eager_fallback(data, name, ctx):
  raise RuntimeError("ref_exit op does not support eager execution. Arg 'output' is a ref.")
_RefMergeOutput = collections.namedtuple(
    "RefMerge",
    ["output", "value_index"])


def ref_merge(inputs, name=None):
  r"""Forwards the value of an available tensor from `inputs` to `output`.

  `Merge` waits for at least one of the tensors in `inputs` to become available.
  It is usually combined with `Switch` to implement branching.

  `Merge` forwards the first tensor for become available to `output`, and sets
  `value_index` to its index in `inputs`.

  Args:
    inputs: A list of at least 1 mutable `Tensor` objects with the same type.
      The input tensors, exactly one of which will become available.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, value_index).

    output: A mutable `Tensor`. Has the same type as `inputs`.
    value_index: A `Tensor` of type `int32`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_merge op does not support eager execution. Arg 'output' is a ref.")
  # Add nodes to the TensorFlow graph.
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'ref_merge' Op, not %r." % inputs)
  _attr_N = len(inputs)
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefMerge", inputs=inputs, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "N", _op._get_attr_int("N"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefMerge", _inputs_flat, _attrs, _result)
  _result = _RefMergeOutput._make(_result)
  return _result

RefMerge = tf_export("raw_ops.RefMerge")(_ops.to_raw_op(ref_merge))


def ref_merge_eager_fallback(inputs, name, ctx):
  raise RuntimeError("ref_merge op does not support eager execution. Arg 'output' is a ref.")

def ref_next_iteration(data, name=None):
  r"""Makes its input available to the next iteration.

  Args:
    data: A mutable `Tensor`.
      The tensor to be made available to the next iteration.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_next_iteration op does not support eager execution. Arg 'output' is a ref.")
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefNextIteration", data=data, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefNextIteration", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RefNextIteration = tf_export("raw_ops.RefNextIteration")(_ops.to_raw_op(ref_next_iteration))


def ref_next_iteration_eager_fallback(data, name, ctx):
  raise RuntimeError("ref_next_iteration op does not support eager execution. Arg 'output' is a ref.")

def ref_select(index, inputs, name=None):
  r"""Forwards the `index`th element of `inputs` to `output`.

  Args:
    index: A `Tensor` of type `int32`.
      A scalar that determines the input that gets selected.
    inputs: A list of at least 1 mutable `Tensor` objects with the same type.
      A list of ref tensors, one of which will be forwarded to `output`.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `inputs`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_select op does not support eager execution. Arg 'output' is a ref.")
  # Add nodes to the TensorFlow graph.
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'ref_select' Op, not %r." % inputs)
  _attr_N = len(inputs)
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefSelect", index=index, inputs=inputs, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "N", _op._get_attr_int("N"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefSelect", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

RefSelect = tf_export("raw_ops.RefSelect")(_ops.to_raw_op(ref_select))


def ref_select_eager_fallback(index, inputs, name, ctx):
  raise RuntimeError("ref_select op does not support eager execution. Arg 'output' is a ref.")
_RefSwitchOutput = collections.namedtuple(
    "RefSwitch",
    ["output_false", "output_true"])


def ref_switch(data, pred, name=None):
  r"""Forwards the ref tensor `data` to the output port determined by `pred`.

  If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
  the data goes to `output_false`.

  See also `Switch` and `Merge`.

  Args:
    data: A mutable `Tensor`.
      The ref tensor to be forwarded to the appropriate output.
    pred: A `Tensor` of type `bool`.
      A scalar that specifies which output port will receive data.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_false, output_true).

    output_false: A mutable `Tensor`. Has the same type as `data`.
    output_true: A mutable `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    raise RuntimeError("ref_switch op does not support eager execution. Arg 'output_true' is a ref.")
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "RefSwitch", data=data, pred=pred, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "RefSwitch", _inputs_flat, _attrs, _result)
  _result = _RefSwitchOutput._make(_result)
  return _result

RefSwitch = tf_export("raw_ops.RefSwitch")(_ops.to_raw_op(ref_switch))


def ref_switch_eager_fallback(data, pred, name, ctx):
  raise RuntimeError("ref_switch op does not support eager execution. Arg 'output_true' is a ref.")
_SwitchOutput = collections.namedtuple(
    "Switch",
    ["output_false", "output_true"])


def switch(data, pred, name=None):
  r"""Forwards `data` to the output port determined by `pred`.

  If `pred` is true, the `data` input is forwarded to `output_true`. Otherwise,
  the data goes to `output_false`.

  See also `RefSwitch` and `Merge`.

  Args:
    data: A `Tensor`. The tensor to be forwarded to the appropriate output.
    pred: A `Tensor` of type `bool`.
      A scalar that specifies which output port will receive data.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output_false, output_true).

    output_false: A `Tensor`. Has the same type as `data`.
    output_true: A `Tensor`. Has the same type as `data`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Switch", name,
        tld.op_callbacks, data, pred)
      _result = _SwitchOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return switch_eager_fallback(
            data, pred, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Switch", data=data, pred=pred, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Switch", _inputs_flat, _attrs, _result)
  _result = _SwitchOutput._make(_result)
  return _result

Switch = tf_export("raw_ops.Switch")(_ops.to_raw_op(switch))


def switch_eager_fallback(data, pred, name, ctx):
  _attr_T, (data,) = _execute.args_to_matching_eager([data], ctx)
  pred = _ops.convert_to_tensor(pred, _dtypes.bool)
  _inputs_flat = [data, pred]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"Switch", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Switch", _inputs_flat, _attrs, _result)
  _result = _SwitchOutput._make(_result)
  return _result

