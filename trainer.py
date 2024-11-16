import torch
import torch.optim as optim
import numpy as np
from model import PasswordCrackingModel
from environment import PasswordCrackingEnv
import torch.nn as nn
from wordlist_loader import load_wordlist

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def train_model(target_password, char_space, wordlist_path, num_episodes=1000):
    input_size = len(target_password)
    output_size = len(char_space)
    
    # Move model to GPU if available
    model = PasswordCrackingModel(input_size, output_size).to(device)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()

    # Load wordlist for training
    wordlist = load_wordlist(wordlist_path)

    # Training loop
    for episode in range(num_episodes):
        # Pick a random password from the wordlist to crack
        target_password = np.random.choice(wordlist)

        env = PasswordCrackingEnv(target_password, char_space)
        state = env.reset()
        
        total_reward = 0
        done = False
        while not done:
            # Convert state to tensor and move to GPU
            state_tensor = torch.tensor([ord(c) for c in state], dtype=torch.float32).unsqueeze(0).to(device)
            
            # Get model action probabilities
            action_probs = model(state_tensor)
            action = torch.multinomial(action_probs, 1).item()
            
            # Take action in the environment
            next_state, reward, done, _ = env.step(action)
            
            # Compute loss
            reward_tensor = torch.tensor([reward], dtype=torch.float32).to(device)
            loss = loss_fn(action_probs, reward_tensor)
            
            # Backpropagate
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_reward += reward
            state = next_state
        
        print(f"Episode {episode + 1}, Total Reward: {total_reward}")
        
    # Save the trained model
    torch.save(model.state_dict(), "password_cracking_model.pth")
