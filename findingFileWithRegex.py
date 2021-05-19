# write a program with regex to search for user provided pattern
# open a directory
# open any .txt file that is currently in the directory
# ask user to provide a pattern which will become the regex
# search within .txt file for the regex
# print results to screen

import glob, os, re, sys
from pathlib import Path

def userRegex(userInput, file):
    findRegex = re.compile(userInput, re.I) # ignore case sensitive
    mo = findRegex.search(file)
    if mo != None:
        print("Found the pattern here:")
        print(mo)
        print(mo.group())
    else:
        print("Nothing found.")

while True:
    os.chdir('C://Users//yourusername//folderpath') #input your own username and folder name, what is the best effective way to set the directory to specific path os.getcwd()?
    for file in glob.glob("*.txt"):
        openFile = open(file)
        fileContent = openFile.read()
        openFile.close()

    userInput = input("Give me a pattern that you want to find. Eg. cats, xxx-xxx-xxxx for phone number, etc. ")
    p = userRegex(userInput, fileContent)
    userQuit = input("Enter Q to quit if you want to exit. ")
    if userQuit.upper() != "Q":
        continue
    else:
        sys.exit() # exit as an alternative 





