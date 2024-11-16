class PasswordCrackingEnv:
    def __init__(self, target_password, char_space):
        self.target_password = target_password
        self.char_space = char_space
        self.state = ""

    def reset(self):
        # Ensure the state is initialized properly with the target password
        self.state = self.target_password
        return self.state

    def step(self, action):
        # For simplicity, we simulate the process of cracking the password here
        # Check if the action matches the target password (you can refine this logic)
        next_state = self.state
        reward = 0
        done = False

        # Simulate checking the action (this can be expanded to actual password matching)
        if action < len(self.state):
            reward = 1  # Reward for correct action
        else:
            reward = -1  # Penalty for incorrect action

        # Check if the password is cracked
        if next_state == self.target_password:
            done = True

        return next_state, reward, done, {}

