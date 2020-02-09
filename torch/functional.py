import torch
import torch.nn.functional as F
from torch._six import inf
from operator import mul
from functools import reduce
import math

__all__ = [
    'argmax',
    'argmin',
    'btrifact',
    'btriunpack',
    'isfinite',
    'isinf',
    'isnan',
    'split',
    'stft',
    'unique',
]


def split(tensor, split_size_or_sections, dim=0):
    r"""Splits the tensor into chunks.

    If :attr:`split_size_or_sections` is an integer type, then :attr:`tensor` will
    be split into equally sized chunks (if possible). Last chunk will be smaller if
    the tensor size along the given dimension :attr:`dim= is not divisible by
    :attr:`split_size`.

    If :attr:`split_size_or_sections` is a list, then :attr:`tensor` will be split
    into ``len(split_size_or_sections)`` chunks with sizes in :attr:`dim` according
    to :attr:`split_size_or_sections`.

    Arguments:
        tensor (Tensor): tensor to split.
        split_size_or_sections (int) or (list(int)): size of a single chunk or
            list of sizes for each chunk
        dim (int): dimension along which to split the tensor.
    """
    # Overwriting reason:
    # This dispatches to two ATen functions depending on the type of
    # split_size_or_sections. The branching code is in tensor.py, which we
    # call here.
    return tensor.split(split_size_or_sections, dim)


def btrifact(A, info=None, pivot=True):
    r"""Batch LU factorization.

    Returns a tuple containing the LU factorization and pivots. Pivoting is done if
    :attr:`pivot` is set.

    The optional argument :attr:`info` stores information if the factorization
    succeeded for each minibatch example. The :attr:`info` is provided as an
    `IntTensor`, its values will be filled from dgetrf and a non-zero value
    indicates an error occurred. Specifically, the values are from cublas if cuda is
    being used, otherwise LAPACK.

    .. warning::
        The :attr:`info` argument is deprecated in favor of :meth:`torch.btrifact_with_info`.

    Arguments:
        A (Tensor): the tensor to factor
        info (IntTensor, optional): (deprecated) an `IntTensor` to store values
            indicating whether factorization succeeds
        pivot (bool, optional): controls whether pivoting is done

    Returns:
        A tuple containing factorization and pivots.

    Example::

        >>> A = torch.randn(2, 3, 3)
        >>> A_LU, pivots = torch.btrifact(A)
        >>> A_LU
        tensor([[[ 1.3506,  2.5558, -0.0816],
                 [ 0.1684,  1.1551,  0.1940],
                 [ 0.1193,  0.6189, -0.5497]],

                [[ 0.4526,  1.2526, -0.3285],
                 [-0.7988,  0.7175, -0.9701],
                 [ 0.2634, -0.9255, -0.3459]]])

        >>> pivots
        tensor([[ 3,  3,  3],
                [ 3,  3,  3]], dtype=torch.int32)
    """
    # Overwriting reason:
    # `info` is being deprecated in favor of `btrifact_with_info`. This warning
    # is in tensor.py, which we call here.
    return A.btrifact(info, pivot)


def btriunpack(LU_data, LU_pivots, unpack_data=True, unpack_pivots=True):
    r"""Unpacks the data and pivots from a batched LU factorization (btrifact) of a tensor.

    Returns a tuple of tensors as ``(the pivots, the L tensor, the U tensor)``.

    Arguments:
        LU_data (Tensor): the packed LU factorization data
        LU_pivots (Tensor): the packed LU factorization pivots
        unpack_data (bool): flag indicating if the data should be unpacked
        unpack_pivots (bool): flag indicating if the pivots should be unpacked

    Example::

        >>> A = torch.randn(2, 3, 3)
        >>> A_LU, pivots = A.btrifact()
        >>> P, A_L, A_U = torch.btriunpack(A_LU, pivots)
        >>>
        >>> # can recover A from factorization
        >>> A_ = torch.bmm(P, torch.bmm(A_L, A_U))
    """

    nBatch, sz, _ = LU_data.size()

    if unpack_data:
        I_U = torch.triu(torch.ones(sz, sz)).type_as(LU_data).byte().unsqueeze(0).expand(nBatch, sz, sz)
        I_L = 1 - I_U
        L = LU_data.new(LU_data.size()).zero_()
        U = LU_data.new(LU_data.size()).zero_()
        I_diag = torch.eye(sz).type_as(LU_data).byte().unsqueeze(0).expand(nBatch, sz, sz)
        L[I_diag] = 1.0
        L[I_L] = LU_data[I_L]
        U[I_U] = LU_data[I_U]
    else:
        L = U = None

    if unpack_pivots:
        P = torch.eye(sz).type_as(LU_data).unsqueeze(0).repeat(nBatch, 1, 1)
        for i in range(nBatch):
            for j in range(sz):
                k = int(LU_pivots[i, j] - 1)
                t = P[i, :, j].clone()
                P[i, :, j] = P[i, :, k]
                P[i, :, k] = t
    else:
        P = None

    return P, L, U


def isfinite(tensor):
    r"""Returns a new tensor with boolean elements representing if each element is `Finite` or not.

    Arguments:
        tensor (Tensor): A tensor to check

    Returns:
        Tensor: A ``torch.ByteTensor`` containing a 1 at each location of finite elements and 0 otherwise

    Example::

        >>> torch.isfinite(torch.Tensor([1, float('inf'), 2, float('-inf'), float('nan')]))
        tensor([ 1,  0,  1,  0,  0], dtype=torch.uint8)
    """
    if not isinstance(tensor, torch.Tensor):
        raise ValueError("The argument is not a tensor", str(tensor))
    return (tensor == tensor) & (tensor.abs() != inf)


def isinf(tensor):
    r"""Returns a new tensor with boolean elements representing if each element is `+/-INF` or not.

    Arguments:
        tensor (Tensor): A tensor to check

    Returns:
        Tensor: A ``torch.ByteTensor`` containing a 1 at each location of `+/-INF` elements and 0 otherwise

    Example::

        >>> torch.isinf(torch.Tensor([1, float('inf'), 2, float('-inf'), float('nan')]))
        tensor([ 0,  1,  0,  1,  0], dtype=torch.uint8)
    """
    if not isinstance(tensor, torch.Tensor):
        raise ValueError("The argument is not a tensor", str(tensor))
    return tensor.abs() == inf


def stft(input, n_fft, hop_length=None, win_length=None, window=None,
         center=True, pad_mode='reflect', normalized=False, onesided=True):
    r"""Short-time Fourier transform (STFT).

    Ignoring the optional batch dimension, this method computes the following
    expression:

    .. math::
        X[m, \omega] = \sum_{k = 0}^{\text{win_length}}%
                            window[k]\ input[m \times hop_length + k]\ %
                            e^{- j \frac{2 \pi \cdot \omega k}{\text{win_length}}},

    where :math:`m` is the index of the sliding window, and :math:`\omega` is
    the frequency that :math:`0 \leq \omega < \text{n_fft}`. When
    :attr:`onesided` is the default value ``True``,

    * :attr:`input` must be either a 1-D time sequenceor 2-D a batch of time
      sequences.

    * If :attr:`hop_length` is ``None`` (default), it is treated as equal to
      ``floor(n_fft / 4)``.

    * If :attr:`win_length` is ``None`` (default), it is treated as equal to
      :attr:`n_fft`.

    * :attr:`window` can be a 1-D tensor of size :attr:`win_length`, e.g., from
      :meth:`torch.hann_window`. If :attr:`window` is ``None`` (default), it is
      treated as if having :math:`1` everywhere in the window. If
      :math:`\text{win_length} < \text{n_fft}`, :attr:`window` will be padded on
      both sides to length :attr:`n_fft` before being applied.

    * If :attr:`center` is ``True`` (default), :attr:`input` will be padded on
      both sides so that the :math:`t`-th frame is centered at time
      :math:`t \times \text{hop_length}`. Otherwise, the :math:`t`-th frame
      begins at time  :math:`t \times \text{hop_length}`.

    * :attr:`pad_mode` determines the padding method used on :attr:`input` when
      :attr:`center` is ``True``. See :meth:`torch.nn.functional.pad` for
      all available options. Default is ``"reflect"``.

    * If :attr:`onesided` is ``True`` (default), only values for :math:`\omega`
      in :math:`\left[0, 1, 2, \dots, \left\lfloor \frac{\text{n_fft}}{2} \right\rfloor + 1\right]`
      are returned because the real-to-complex Fourier transform satisfies the
      conjugate symmetry, i.e., :math:`X[m, \omega] = X[m, \text{n_fft} - \omega]^*`.

    * If :attr:`normalized` is ``True`` (default is ``False``), the function
      returns the normalized STFT results, i.e., multiplied by :math:`(\text{frame_length})^{-0.5}`.

    Returns the real and the imaginary parts together as one tensor of size
    :math:`(* \times N \times T \times 2)`, where :math:`*` is the optional
    batch size of :attr:`input`, :math:`N` is the number of frequencies where
    STFT is applied, :math:`T` is the total number of frames used, and each pair
    in the last dimension represents a complex number as the real part and the
    imaginary part.

    .. warning::
      This function changed signature at version 0.4.1. Calling with the
      previous signature may cause error or return incorrect result.

    Arguments:
        input (Tensor): the input tensor
        n_fft (int, optional): size of Fourier transform
        hop_length (int): the distance between neighboring sliding window
            frames. Default: ``None`` (treated as equal to ``floor(n_fft / 4)``)
        win_length (int): the size of window frame and STFT filter.
            Default: ``None``  (treated as equal to :attr:`n_fft`)
        window (Tensor, optional): the optional window function.
            Default: ``None`` (treated as window of all :math:`1`s)
        center (bool, optional): whether to pad :attr:`input` on both sides so
            that the :math:`t`-th frame is centered at time :math:`t \times \text{hop_length}`.
            Default: ``True``
        pad_mode (string, optional): controls the padding method used when
            :attr:`center` is ``True``. Default: ``"reflect"``
        normalized (bool, optional): controls whether to return the normalized STFT results
             Default: ``False``
        onesided (bool, optional): controls whether to return half of results to
            avoid redundancy Default: ``True``

    Returns:
        Tensor: A tensor containing the STFT result with shape described above

    """
    # TODO: after having proper ways to map Python strings to ATen Enum, move
    #       this and F.pad to ATen.
    if center:
        signal_dim = input.dim()
        extended_shape = [1] * (3 - signal_dim) + list(input.size())
        pad = int(n_fft // 2)
        input = F.pad(input.view(extended_shape), (pad, pad), pad_mode)
        input = input.view(input.shape[-signal_dim:])
    return torch._C._VariableFunctions.stft(input, n_fft, hop_length, win_length, window, normalized, onesided)


def isnan(tensor):
    r"""Returns a new tensor with boolean elements representing if each element is `NaN` or not.

    Arguments:
        tensor (Tensor): A tensor to check

    Returns:
        Tensor: A ``torch.ByteTensor`` containing a 1 at each location of `NaN` elements.

    Example::

        >>> torch.isnan(torch.tensor([1, float('nan'), 2]))
        tensor([ 0,  1,  0], dtype=torch.uint8)
    """
    if not isinstance(tensor, torch.Tensor):
        raise ValueError("The argument is not a tensor", str(tensor))
    return tensor != tensor


def unique(input, sorted=False, return_inverse=False):
    r"""Returns the unique scalar elements of the input tensor as a 1-D tensor.

    Arguments:
        input (Tensor): the input tensor
        sorted (bool): Whether to sort the unique elements in ascending order
            before returning as output.
        return_inverse (bool): Whether to also return the indices for where
            elements in the original input ended up in the returned unique list.

    Returns:
        (Tensor, Tensor (optional)): A tensor or a tuple of tensors containing

            - **output** (*Tensor*): the output list of unique scalar elements.
            - **inverse_indices** (*Tensor*): (optional) if
              :attr:`return_inverse` is True, there will be a
              2nd returned tensor (same shape as input) representing the indices
              for where elements in the original input map to in the output;
              otherwise, this function will only return a single tensor.

    Example::

        >>> output = torch.unique(torch.tensor([1, 3, 2, 3], dtype=torch.long))
        >>> output
        tensor([ 2,  3,  1])

        >>> output, inverse_indices = torch.unique(
                torch.tensor([1, 3, 2, 3], dtype=torch.long), sorted=True, return_inverse=True)
        >>> output
        tensor([ 1,  2,  3])
        >>> inverse_indices
        tensor([ 0,  2,  1,  2])

        >>> output, inverse_indices = torch.unique(
                torch.tensor([[1, 3], [2, 3]], dtype=torch.long), sorted=True, return_inverse=True)
        >>> output
        tensor([ 1,  2,  3])
        >>> inverse_indices
        tensor([[ 0,  2],
                [ 1,  2]])

    """
    output, inverse_indices = torch._unique(
        input,
        sorted=sorted,
        return_inverse=return_inverse,
    )
    if return_inverse:
        return output, inverse_indices
    else:
        return output


def argmax(input, dim=None, keepdim=False):
    """Returns the indices of the maximum values of a tensor across a dimension.

    This is the second value returned by :meth:`torch.max`. See its
    documentation for the exact semantics of this method.

    Args:
        input (Tensor): the input tensor
        dim (int): the dimension to reduce. If ``None``, the argmax of the
            flattened input is returned.
        keepdim (bool): whether the output tensors have :attr:`dim`
            retained or not. Ignored if ``dim=None``.

    Example::

        >>> a = torch.randn(4, 4)
        >>> a
        tensor([[ 1.3398,  0.2663, -0.2686,  0.2450],
                [-0.7401, -0.8805, -0.3402, -1.1936],
                [ 0.4907, -1.3948, -1.0691, -0.3132],
                [-1.6092,  0.5419, -0.2993,  0.3195]])


        >>> torch.argmax(a, dim=1)
        tensor([ 0,  2,  0,  1])
    """
    if dim is None:
        return torch._argmax(input.contiguous().view(-1), dim=0, keepdim=False)
    return torch._argmax(input, dim, keepdim)


def argmin(input, dim=None, keepdim=False):
    """Returns the indices of the minimum values of a tensor across a dimension.

    This is the second value returned by :meth:`torch.min`. See its
    documentation for the exact semantics of this method.

    Args:
        input (Tensor): the input tensor
        dim (int): the dimension to reduce. If ``None``, the argmin of the
            flattened input is returned.
        keepdim (bool): whether the output tensors have :attr:`dim`
            retained or not. Ignored if ``dim=None``.

    Example::

        >>> a = torch.randn(4, 4)
        >>> a
        tensor([[ 0.1139,  0.2254, -0.1381,  0.3687],
                [ 1.0100, -1.1975, -0.0102, -0.4732],
                [-0.9240,  0.1207, -0.7506, -1.0213],
                [ 1.7809, -1.2960,  0.9384,  0.1438]])


        >>> torch.argmin(a, dim=1)
        tensor([ 2,  1,  3,  1])
    """
    if dim is None:
        return torch._argmin(input.contiguous().view(-1), dim=0, keepdim=False)
    return torch._argmin(input, dim, keepdim)
