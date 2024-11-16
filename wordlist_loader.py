def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r') as file:
        wordlist = file.readlines()
    return [word.strip() for word in wordlist]
