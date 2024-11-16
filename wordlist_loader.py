def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
        wordlist = file.readlines()
    return wordlist
