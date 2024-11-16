from trainer import train_model

# Define the character space (can be extended to more characters if needed)
char_space = list("abcdefghijklmnopqrstuvwxyz0123456789")  # Lowercase + numbers

# Path to your wordlist (e.g., rockyou.txt)
wordlist_path = "rockyou.txt"  # Change this to the path of your wordlist file

# Train the model
train_model(target_password=None, char_space=char_space, wordlist_path=wordlist_path)
