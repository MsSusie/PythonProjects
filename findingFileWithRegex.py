import glob, os, re, sys
from pathlib import Path

# set up regex to search for user provided pattern
# open directory
# open any .txt file that is currently in the directory
# use the regex
# print results to screen

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
    os.chdir('C://Users//yourusername//folderpath') #input your own username and folder name
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
        sys.exit()





