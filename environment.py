import random

class PasswordCrackingEnv:
    def __init__(self, target_password, char_space):
        self.target_password = target_password
        self.char_space = char_space
        self.state = ""
        self.max_length = len(target_password)
        self.current_length = 0
    
    def reset(self):
        self.state = ""
        self.current_length = 0
        return self.state
    
    def step(self, action):
        # Append the character at the action position
        next_char = self.char_space[action]
        self.state += next_char
        self.current_length += 1
        
        # Calculate reward based on how close the guess is to the target password
        reward = 0
        if self.state == self.target_password:
            reward = 1  # Successfully cracked the password
            done = True
        elif self.state == self.target_password[:self.current_length]:
            reward = 0.1  # Progress is being made
            done = False
        else:
            reward = -0.1  # Wrong progress
            done = False
        
        return self.state, reward, done, {}
