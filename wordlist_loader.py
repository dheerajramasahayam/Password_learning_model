def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        wordlist = [line.strip() for line in f.readlines()]
    return wordlist
