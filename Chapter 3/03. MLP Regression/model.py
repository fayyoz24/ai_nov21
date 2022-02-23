import torch
import torch.nn.functional as F
from torch import nn


# YOUR CODE HERE

class FullyConnected(nn.Module):
    def __init__(self, in_dim, out_dim):
        super(FullyConnected, self).__init__()
        self.input_layer    = nn.Linear(in_dim, 4)
        self.hidden1        = nn.Linear(4, 8)
        self.hidden2        = nn.Linear(8, 8)
        self.output_layer   = nn.Linear(8, out_dim)
        self.sigmoid        = nn.Sigmoid()
    
    def forward(self, x):
        out0 = self.sigmoid(self.input_layer(x))    # sigmoid(W @ X + b)
        out1 = self.sigmoid(self.hidden1(out0))
        out2 = self.sigmoid(self.hidden2(out1))

        return self.sigmoid(self.output_layer(out2))




        