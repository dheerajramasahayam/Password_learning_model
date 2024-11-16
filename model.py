import torch
import torch.nn as nn

class PasswordCrackingModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(PasswordCrackingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)  # First hidden layer
        self.fc2 = nn.Linear(128, output_size)  # Output layer

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Apply ReLU to first layer
        x = self.fc2(x)  # Output layer
        return x
