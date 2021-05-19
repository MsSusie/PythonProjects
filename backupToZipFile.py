#! python3
# backing up a folder into a zip file
# save zip file with incremental numbers in the filename

import zipfile, os

def backupToZip(folder):
    print(os.path.abspath(folder))

    # back up entire contents of folder into zip file
    folder = os.path.abspath(folder) # check to see if folder is in absolute path

    # figure out the filename this code should use is based on what files already exist
    number = 1 # first file
    while True:
        # where basename(folder) specifies basename (tail) from the path
        zipFileName = os.path.basename(folder) + '_' + str(number)+'.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1

    # create the zip file
    print(f'Creating the ZIP file {zipFileName}...')
    backupZIP = zipfile.ZipFile(zipFileName, 'w')

    # walk the folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        # add the current folder to the zip file
        backupZIP.write(foldername)

        #add all the files in this folder to the zip file
        for filename in filenames:
            newBase = os.path.basename(folder)+ '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the zip file that was already backed up
            backupZIP.write(os.path.join(foldername, filename))

    backupZIP.close()
    print("Done.")


backupToZip('C://Users//') #calling the function, enter in your folder name here


