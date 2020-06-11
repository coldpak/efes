import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F


class SimpleNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleNet, self).__init__()
        self.linear1 = nn.Linear(input_dim, hidden_dim)
        self.linear2 = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        h_relu = F.relu(self.linear1(x))
        y_pred = self.linear2(h_relu)

        return y_pred


if __name__ == '__main__':
    N, D_in, H, D_out = 32, 100, 50, 10
    x = Variable(torch.randn(N, D_in))
    model = SimpleNet(D_in, H, D_out)
    y_pred = model(x)
    print(y_pred.size())
