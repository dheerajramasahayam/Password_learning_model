import torch
import numpy as np
from trainer import train_model

if __name__ == "__main__":
    # Define your target password, character space, and wordlist path
    target_password = "examplepassword"  # Example password, replace with your target password
    char_space = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Example char space
    wordlist_path = "path/to/your/wordlist.txt"  # Replace with actual path to your wordlist

    # Start training the model
    train_model(target_password=target_password, char_space=char_space, wordlist_path=wordlist_path)
