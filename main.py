from trainer import train_model

# Define the character space (can be extended to more characters if needed)
char_space = list("abcdefghijklmnopqrstuvwxyz0123456789")  # Lowercase + numbers

# Path to your wordlist (e.g., rockyou.txt)
wordlist_path = "rockyou.txt"  # Change this to the path of your wordlist file

# Select a random password from the wordlist as target_password
import random
wordlist = open(wordlist_path, 'r', encoding='utf-8', errors='ignore').readlines()
target_password = random.choice(wordlist).strip()

# Train the model
train_model(target_password=target_password, char_space=char_space, wordlist_path=wordlist_path)
