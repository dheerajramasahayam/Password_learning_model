import torch
import torch.nn as nn

class PasswordCrackingModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(PasswordCrackingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)  # input_size should match the length of the target password
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, output_size)
        self.softmax = nn.Softmax(dim=1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return self.softmax(x)
