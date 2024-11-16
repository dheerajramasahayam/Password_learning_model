import gym
import numpy as np

class PasswordCrackingEnv(gym.Env):
    def __init__(self, target_password, char_space):
        super(PasswordCrackingEnv, self).__init__()
        self.target_password = target_password
        self.char_space = char_space
        self.max_length = len(target_password)
        self.current_guess = ['_'] * self.max_length
        self.done = False
        self.reward = 0
        
        # Action space: One of the characters in the character space
        self.action_space = gym.spaces.Discrete(len(char_space))
        
        # Observation space: the current guess
        self.observation_space = gym.spaces.Discrete(len(char_space)**self.max_length)
        
    def reset(self):
        self.current_guess = ['_'] * self.max_length
        self.done = False
        return ''.join(self.current_guess)
    
    def step(self, action):
        if self.done:
            return ''.join(self.current_guess), self.reward, self.done, {}
        
        # Map action to character
        guess_char = self.char_space[action]
        self.current_guess = self.current_guess[:action] + [guess_char] + self.current_guess[action+1:]
        
        # Reward is given if the character matches the target password
        correct_char = self.target_password[action]
        self.reward = 1 if guess_char == correct_char else -1
        
        # Check if the password is fully guessed
        if ''.join(self.current_guess) == self.target_password:
            self.done = True
            self.reward = 10  # Give a large reward for full guess
        
        return ''.join(self.current_guess), self.reward, self.done, {}
