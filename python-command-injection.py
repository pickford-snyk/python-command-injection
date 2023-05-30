import os

folder = input("Enter folder name: ")

def getFolders():
    folders = os.popen(f"ls ~/{folder}").read().split('/n')
    return list(filter(None,folders))

print(getFolders())