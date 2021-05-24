#! python3
# program to delete files from folder or the whole folder
# this program will not actually delete but will print to screen the files that it found (to prevent accidentally deleting files)
# use send2trash module for safe delete to recycle bin

import os, send2trash, sys
from pathlib import Path

while True:
    userFileType = input("Do you want to delete a file or a folder? Please type in File or Folder as an answer. ")
    if not userFileType.isalpha():
        print("Only input File or Folder, please.")
        continue

    userFileSize = input("What is the minimum size in bytes that you want deleted? ")
    userFileSizeMax = input("What is the max size in bytes that you want deleted? ")
    userFilePath = input("Where is the filepath that you want these files/folders deleted from? ")

    if not os.path.exists(userFilePath):
        print("Please try putting in a valid absolute path.")
        continue

    path = os.path.abspath(userFilePath)
    print('')

    userConfirm = input("To confirm, this is the filepath that you want deleted. " + str(path) + "       Please write Y or N: ")
    if userConfirm.upper() == "N":
        userFilePath = input("Where is the filepath that you want these files/folders deleted from? ")
    print('')

    # if user chose to delete folders
    if userFileType.upper() != "FILE":
        totalSize = 0
        startPath = '.' # get size of current directory
        filePath = path

        for path, dirs, files in os.walk(startPath):
            for f in files:
                if not os.path.islink(filePath):
                    totalSize += os.path.getsize(filePath)

                print(totalSize)

                if int(totalSize) >= int(userFileSize) and int(totalSize) <= int(userFileSizeMax):
                    print("Found the folder/s whose size is at least " + str(userFileSize) + " and at max " + str(userFileSizeMax) + ":" + os.path.dirname(path))
                    # send2trash.send2trash(dir)   # this deletes folder, uncomment the code out to implement it
                    print('')

                else:
                    print("Found no folders matching around that size.")
                    print('')

        if totalSize == 0:
            print("This filepath has no size. ")
            sys.exit("This program is exiting.")

    # if user chose to delete files
    else:
        for folders, subfolders, files in os.walk(path):
            for folder in folders:
                for subfolder in subfolders:
                    for file in files:
                        fileSize = os.path.getsize(os.path.join(path, file))
                        print('File size: ' + str(fileSize))

                        if int(fileSize) >= int(userFileSize) and int(fileSize) <= int(userFileSizeMax):
                            print(f'Found the matching file size to delete: ' + file )
                            print('')
                            # send2trash.send2trash(file)   #uncomment the code to actually delete the file
                        else:
                            print("Found no file/s with matching size/s to delete.")
                            print('')

    sys.exit("Program is exiting now.")





