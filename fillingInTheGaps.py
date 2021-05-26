# python 3
# program that finds all files with a given prefix eg. spam001.txt, spam002.txt, spam004.txt etc and
# locates any gaps in the numbering eg. missing spam003.txt when the file jumps to spam004.txt
# program should rename all the later files to close the gaps

import re, os, glob, shutil
from pathlib import Path


while True:

    userPathInput = input("Where is the file path that you want to check? ")
    filePath = os.chdir(userPathInput)

    p = Path(userPathInput)
    pathExists = os.path.exists(p)

    if not pathExists:
        print("That file path does not exist. Try again.")
        print('')
        continue
    else:
        for folders, subfolders, files in sorted(os.walk(p)):               # traverse each file in folder and reads filename
            for file in files:

                fileRegex = re.compile(r'(\w{1,})(\d{1,})(.\w+)')
                fileMO = fileRegex.search(file)

                if fileMO == None:
                    print("Not a match.")

                else:
                    print(fileMO.group())

                    prefix = fileMO.group(1)  # if file 'eggs001.txt' then prefix = eggs00
                    numberInFile = int(fileMO.group(2))     # if file 'eggs001.txt' then numberInFile = 1
                    suffix = fileMO.group(3) # extension of file
                    counter = numberInFile # use this to check against the file number pulled from fileMO.group(2) to check for gaps, starts at whatever the smallest file number is

                    for i in range(len(glob.glob('*[0-9].txt'))):

                        if numberInFile != counter:  # finds the gap in the numbering by comparing file number against counter
                            renamedFile = prefix + str(counter) + suffix    # rename the file by putting together the pieces
                            if not os.path.exists(renamedFile):
                                print(renamedFile)                              # test to see if it renamed correctly
                                shutil.move(os.path.abspath(file), os.path.abspath(renamedFile))
                                counter += 1



        break


