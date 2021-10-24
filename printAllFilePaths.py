import os

def printAllFilepaths(directory):
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            filepath = subdir + os.sep + filename
            if filepath.endswith(".txt"):
                print(filepath)