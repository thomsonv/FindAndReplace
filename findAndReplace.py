""" 1/25/2018:
Problem: Have loads of log files with multiple 'keys'.
The log file processing tool does not recognize 'key' strings but wants 'code' strings!

Solution: Write a python based tool, were a user can define list of strings that they want
replaced over mutiple files in one directory """

import os
import csv

# Opening the directory and reading all the file names
myDir = input("Input the path of directory where and Find and Replace operation is desired : ")
allFiles = os.listdir(myDir)

# reading find and replace csv file into a list
with open('findAndReplace.csv', 'r') as f:
    reader = csv.reader(f)
    ourList = list(reader)

#openning one file at a time
for currentFile in allFiles:
    currentFile=myDir+'/'+currentFile
    with open(currentFile, 'r') as file :
        filedata = file.read()
        print('Opening file %s' % currentFile)
        #finding and replacing all the strings in the file
        for list in ourList:
            print('Finding %s and replacing it with %s' % (list[0], list[1]))
            filedata = filedata.replace(list[0], list[1])
            # Write the file out again
            with open(currentFile, 'w') as file:
                file.write(filedata)

a = input(" Hit ENTER to end this program")
