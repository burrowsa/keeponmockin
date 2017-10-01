def count_words(filename):
    words = 0
    with open(filename) as f:
        for line in f.readlines():
            words += sum(1 for word in line.strip().split(' ') if word)
    return words

def count_words_alt(filename):
    words = 0
    with open(filename) as f:
        for line in f:
            words += sum(1 for word in line.strip().split(' ') if word)
    return words
