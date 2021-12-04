import os

def allFilesCount(dir, counter=0):
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return dir + " : " + str(counter) + " files"

def txtFileCountInSubdirectories():
    file_count = sum(len(files) for _, _, files in os.walk(r'articles'))
    print(file_count)