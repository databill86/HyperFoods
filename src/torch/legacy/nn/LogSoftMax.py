import torch
from .Module import Module


class LogSoftMax(Module):

    def __init__(self, dim=None):
        super(LogSoftMax, self).__init__()
        if dim is not None:
            self.dim = dim

    def _get_dim(self, input):
        return getattr(self, 'dim', 0 if input.dim() == 1 or input.dim() == 3 else 1)

    def updateOutput(self, input):
        self.output = torch.log_softmax(
            input,
            self._get_dim(input)
        )
        return self.output

    def updateGradInput(self, input, gradOutput):
        self.gradInput = torch.log_softmax_backward_data(
            gradOutput,
            self.output,
            self._get_dim(input),
            input
        )
        return self.gradInput
