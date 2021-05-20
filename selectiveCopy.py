#! python 3
#  program that walks through folder tree and searches for files with certain file ext (.txt)
#  copy the files from source into destination

import shutil, os, glob
from pathlib import Path

def fileFinder(folder, destination):

    os.chdir(folder)

    # traverse the folder tree
    # copy files and move to new folder shutil.copy()
    for folders, subFolders, filenames in os.walk(folder):
        for folder in folders:
            for subFolder in subFolders: # code around here may need to be revised? for subfolders of a folder they are not copying any .txt files
                for filename in filenames:
                    if filename.endswith('.txt'):
                        shutil.copy(filename, destination)
    print("All .txt files copied over.")


while True:
    # get input from user for source filepath
    sourceInput = input("Give a source filepath. ")

    if not os.path.exists(sourceInput):
        print("Please put in a valid absolute filepath. ")
        continue

    destinationInput = input("Give a destination filepath. ")
    if not os.path.exists(destinationInput):
        os.mkdir(destinationInput)

    # call the function
    fileFinder(sourceInput,destinationInput)
    break







