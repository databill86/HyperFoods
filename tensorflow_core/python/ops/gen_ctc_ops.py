"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: ctc_ops.cc
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

_CTCBeamSearchDecoderOutput = collections.namedtuple(
    "CTCBeamSearchDecoder",
    ["decoded_indices", "decoded_values", "decoded_shape", "log_probability"])


def ctc_beam_search_decoder(inputs, sequence_length, beam_width, top_paths, merge_repeated=True, name=None):
  r"""Performs beam search decoding on the logits given in input.

  A note about the attribute merge_repeated: For the beam search decoder,
  this means that if consecutive entries in a beam are the same, only
  the first of these is emitted.  That is, when the top path is "A B B B B",
  "A B" is returned if merge_repeated = True but "A B B B B" is
  returned if merge_repeated = False.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths, size `(batch)`.
    beam_width: An `int` that is `>= 1`.
      A scalar >= 0 (beam search beam width).
    top_paths: An `int` that is `>= 1`.
      A scalar >= 0, <= beam_width (controls output size).
    merge_repeated: An optional `bool`. Defaults to `True`.
      If true, merge repeated classes in output.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (decoded_indices, decoded_values, decoded_shape, log_probability).

    decoded_indices: A list of `top_paths` `Tensor` objects with type `int64`.
    decoded_values: A list of `top_paths` `Tensor` objects with type `int64`.
    decoded_shape: A list of `top_paths` `Tensor` objects with type `int64`.
    log_probability: A `Tensor`. Has the same type as `inputs`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "CTCBeamSearchDecoder", name,
        tld.op_callbacks, inputs, sequence_length, "beam_width", beam_width,
        "top_paths", top_paths, "merge_repeated", merge_repeated)
      _result = _CTCBeamSearchDecoderOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return ctc_beam_search_decoder_eager_fallback(
            inputs, sequence_length, beam_width=beam_width,
            top_paths=top_paths, merge_repeated=merge_repeated, name=name,
            ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  beam_width = _execute.make_int(beam_width, "beam_width")
  top_paths = _execute.make_int(top_paths, "top_paths")
  if merge_repeated is None:
    merge_repeated = True
  merge_repeated = _execute.make_bool(merge_repeated, "merge_repeated")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "CTCBeamSearchDecoder", inputs=inputs,
                                sequence_length=sequence_length,
                                beam_width=beam_width, top_paths=top_paths,
                                merge_repeated=merge_repeated, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("beam_width", _op._get_attr_int("beam_width"), "top_paths",
              _op._get_attr_int("top_paths"), "merge_repeated",
              _op._get_attr_bool("merge_repeated"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "CTCBeamSearchDecoder", _inputs_flat, _attrs, _result)
  _result = [_result[:top_paths]] + _result[top_paths:]
  _result = _result[:1] + [_result[1:1 + top_paths]] + _result[1 + top_paths:]
  _result = _result[:2] + [_result[2:2 + top_paths]] + _result[2 + top_paths:]
  _result = _CTCBeamSearchDecoderOutput._make(_result)
  return _result

CTCBeamSearchDecoder = tf_export("raw_ops.CTCBeamSearchDecoder")(_ops.to_raw_op(ctc_beam_search_decoder))


def ctc_beam_search_decoder_eager_fallback(inputs, sequence_length, beam_width, top_paths, merge_repeated, name, ctx):
  beam_width = _execute.make_int(beam_width, "beam_width")
  top_paths = _execute.make_int(top_paths, "top_paths")
  if merge_repeated is None:
    merge_repeated = True
  merge_repeated = _execute.make_bool(merge_repeated, "merge_repeated")
  _attr_T, (inputs,) = _execute.args_to_matching_eager([inputs], ctx, _dtypes.float32)
  sequence_length = _ops.convert_to_tensor(sequence_length, _dtypes.int32)
  _inputs_flat = [inputs, sequence_length]
  _attrs = ("beam_width", beam_width, "top_paths", top_paths,
  "merge_repeated", merge_repeated, "T", _attr_T)
  _result = _execute.execute(b"CTCBeamSearchDecoder", top_paths + top_paths +
                             top_paths + 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "CTCBeamSearchDecoder", _inputs_flat, _attrs, _result)
  _result = [_result[:top_paths]] + _result[top_paths:]
  _result = _result[:1] + [_result[1:1 + top_paths]] + _result[1 + top_paths:]
  _result = _result[:2] + [_result[2:2 + top_paths]] + _result[2 + top_paths:]
  _result = _CTCBeamSearchDecoderOutput._make(_result)
  return _result

_CTCGreedyDecoderOutput = collections.namedtuple(
    "CTCGreedyDecoder",
    ["decoded_indices", "decoded_values", "decoded_shape", "log_probability"])


def ctc_greedy_decoder(inputs, sequence_length, merge_repeated=False, name=None):
  r"""Performs greedy decoding on the logits given in inputs.

  A note about the attribute merge_repeated: if enabled, when
  consecutive logits' maximum indices are the same, only the first of
  these is emitted.  Labeling the blank '*', the sequence "A B B * B B"
  becomes "A B B" if merge_repeated = True and "A B B B B" if
  merge_repeated = False.

  Regardless of the value of merge_repeated, if the maximum index of a given
  time and batch corresponds to the blank, index `(num_classes - 1)`, no new
  element is emitted.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths, size `(batch_size)`.
    merge_repeated: An optional `bool`. Defaults to `False`.
      If True, merge repeated classes in output.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (decoded_indices, decoded_values, decoded_shape, log_probability).

    decoded_indices: A `Tensor` of type `int64`.
    decoded_values: A `Tensor` of type `int64`.
    decoded_shape: A `Tensor` of type `int64`.
    log_probability: A `Tensor`. Has the same type as `inputs`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "CTCGreedyDecoder", name,
        tld.op_callbacks, inputs, sequence_length, "merge_repeated",
        merge_repeated)
      _result = _CTCGreedyDecoderOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return ctc_greedy_decoder_eager_fallback(
            inputs, sequence_length, merge_repeated=merge_repeated, name=name,
            ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if merge_repeated is None:
    merge_repeated = False
  merge_repeated = _execute.make_bool(merge_repeated, "merge_repeated")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "CTCGreedyDecoder", inputs=inputs, sequence_length=sequence_length,
                            merge_repeated=merge_repeated, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("merge_repeated", _op._get_attr_bool("merge_repeated"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "CTCGreedyDecoder", _inputs_flat, _attrs, _result)
  _result = _CTCGreedyDecoderOutput._make(_result)
  return _result

CTCGreedyDecoder = tf_export("raw_ops.CTCGreedyDecoder")(_ops.to_raw_op(ctc_greedy_decoder))


def ctc_greedy_decoder_eager_fallback(inputs, sequence_length, merge_repeated, name, ctx):
  if merge_repeated is None:
    merge_repeated = False
  merge_repeated = _execute.make_bool(merge_repeated, "merge_repeated")
  _attr_T, (inputs,) = _execute.args_to_matching_eager([inputs], ctx, _dtypes.float32)
  sequence_length = _ops.convert_to_tensor(sequence_length, _dtypes.int32)
  _inputs_flat = [inputs, sequence_length]
  _attrs = ("merge_repeated", merge_repeated, "T", _attr_T)
  _result = _execute.execute(b"CTCGreedyDecoder", 4, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "CTCGreedyDecoder", _inputs_flat, _attrs, _result)
  _result = _CTCGreedyDecoderOutput._make(_result)
  return _result

_CTCLossOutput = collections.namedtuple(
    "CTCLoss",
    ["loss", "gradient"])


def ctc_loss(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated=False, ctc_merge_repeated=True, ignore_longer_outputs_than_inputs=False, name=None):
  r"""Calculates the CTC Loss (log probability) for each batch entry.  Also calculates

  the gradient.  This class performs the softmax operation for you, so inputs
  should be e.g. linear projections of outputs by an LSTM.

  Args:
    inputs: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      3-D, shape: `(max_time x batch_size x num_classes)`, the logits.
    labels_indices: A `Tensor` of type `int64`.
      The indices of a `SparseTensor<int32, 2>`.
      `labels_indices(i, :) == [b, t]` means `labels_values(i)` stores the id for
      `(batch b, time t)`.
    labels_values: A `Tensor` of type `int32`.
      The values (labels) associated with the given batch and time.
    sequence_length: A `Tensor` of type `int32`.
      A vector containing sequence lengths (batch).
    preprocess_collapse_repeated: An optional `bool`. Defaults to `False`.
      Scalar, if true then repeated labels are
      collapsed prior to the CTC calculation.
    ctc_merge_repeated: An optional `bool`. Defaults to `True`.
      Scalar.  If set to false, *during* CTC calculation
      repeated non-blank labels will not be merged and are interpreted as
      individual labels.  This is a simplified version of CTC.
    ignore_longer_outputs_than_inputs: An optional `bool`. Defaults to `False`.
      Scalar. If set to true, during CTC
      calculation, items that have longer output sequences than input sequences
      are skipped: they don't contribute to the loss term and have zero-gradient.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (loss, gradient).

    loss: A `Tensor`. Has the same type as `inputs`.
    gradient: A `Tensor`. Has the same type as `inputs`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = _pywrap_tensorflow.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "CTCLoss", name,
        tld.op_callbacks, inputs, labels_indices, labels_values,
        sequence_length, "preprocess_collapse_repeated",
        preprocess_collapse_repeated, "ctc_merge_repeated",
        ctc_merge_repeated, "ignore_longer_outputs_than_inputs",
        ignore_longer_outputs_than_inputs)
      _result = _CTCLossOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return ctc_loss_eager_fallback(
            inputs, labels_indices, labels_values, sequence_length,
            preprocess_collapse_repeated=preprocess_collapse_repeated,
            ctc_merge_repeated=ctc_merge_repeated,
            ignore_longer_outputs_than_inputs=ignore_longer_outputs_than_inputs,
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if preprocess_collapse_repeated is None:
    preprocess_collapse_repeated = False
  preprocess_collapse_repeated = _execute.make_bool(preprocess_collapse_repeated, "preprocess_collapse_repeated")
  if ctc_merge_repeated is None:
    ctc_merge_repeated = True
  ctc_merge_repeated = _execute.make_bool(ctc_merge_repeated, "ctc_merge_repeated")
  if ignore_longer_outputs_than_inputs is None:
    ignore_longer_outputs_than_inputs = False
  ignore_longer_outputs_than_inputs = _execute.make_bool(ignore_longer_outputs_than_inputs, "ignore_longer_outputs_than_inputs")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "CTCLoss", inputs=inputs, labels_indices=labels_indices,
                   labels_values=labels_values,
                   sequence_length=sequence_length,
                   preprocess_collapse_repeated=preprocess_collapse_repeated,
                   ctc_merge_repeated=ctc_merge_repeated,
                   ignore_longer_outputs_than_inputs=ignore_longer_outputs_than_inputs,
                   name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("preprocess_collapse_repeated",
              _op._get_attr_bool("preprocess_collapse_repeated"),
              "ctc_merge_repeated", _op._get_attr_bool("ctc_merge_repeated"),
              "ignore_longer_outputs_than_inputs",
              _op._get_attr_bool("ignore_longer_outputs_than_inputs"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "CTCLoss", _inputs_flat, _attrs, _result)
  _result = _CTCLossOutput._make(_result)
  return _result

CTCLoss = tf_export("raw_ops.CTCLoss")(_ops.to_raw_op(ctc_loss))


def ctc_loss_eager_fallback(inputs, labels_indices, labels_values, sequence_length, preprocess_collapse_repeated, ctc_merge_repeated, ignore_longer_outputs_than_inputs, name, ctx):
  if preprocess_collapse_repeated is None:
    preprocess_collapse_repeated = False
  preprocess_collapse_repeated = _execute.make_bool(preprocess_collapse_repeated, "preprocess_collapse_repeated")
  if ctc_merge_repeated is None:
    ctc_merge_repeated = True
  ctc_merge_repeated = _execute.make_bool(ctc_merge_repeated, "ctc_merge_repeated")
  if ignore_longer_outputs_than_inputs is None:
    ignore_longer_outputs_than_inputs = False
  ignore_longer_outputs_than_inputs = _execute.make_bool(ignore_longer_outputs_than_inputs, "ignore_longer_outputs_than_inputs")
  _attr_T, (inputs,) = _execute.args_to_matching_eager([inputs], ctx, _dtypes.float32)
  labels_indices = _ops.convert_to_tensor(labels_indices, _dtypes.int64)
  labels_values = _ops.convert_to_tensor(labels_values, _dtypes.int32)
  sequence_length = _ops.convert_to_tensor(sequence_length, _dtypes.int32)
  _inputs_flat = [inputs, labels_indices, labels_values, sequence_length]
  _attrs = ("preprocess_collapse_repeated", preprocess_collapse_repeated,
  "ctc_merge_repeated", ctc_merge_repeated,
  "ignore_longer_outputs_than_inputs", ignore_longer_outputs_than_inputs, "T",
  _attr_T)
  _result = _execute.execute(b"CTCLoss", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "CTCLoss", _inputs_flat, _attrs, _result)
  _result = _CTCLossOutput._make(_result)
  return _result

