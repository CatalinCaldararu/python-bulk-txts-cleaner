def articleWordCount(filename):
    number = 0
    with open(filename, 'r+') as f:
        for line in f:
            words = line.split()
            number += len(words)
    return number