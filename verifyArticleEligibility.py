import os
from pathlib import Path

def isTheArticleEligible(filepath, minWords):
    number = 0
    filename = os.path.basename(filepath)
    with open(Path(filename), 'r+') as f:
        for line in f:
            words = line.split()
            number += len(words)
    if number > minWords:
        return True
    else: return False