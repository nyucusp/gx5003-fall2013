# Awais Malik
# Assignment 2
# Tutorial 1

import sys
collabName = sys.argv[1]

myFile = open('logsofar.txt','r')
outputFile = open('output.txt','w')

state = 0
commitDateTimes = []
for line in myFile:
    if(state == 0):  # Look for author line
        indexofCollab = line.find(collabName)
        if(indexofCollab != -1):  # Found a commit from Collab
            state = 1  # Now find the date and time of this commit
    else:
        indexofDate = line.find("Date:")
        if(indexofDate != -1):  # Found date from the previous commit
            commitDateTimes.append(line)
            state = 0
myFile.close()

for commitDateTime in commitDateTimes:
    outputFile.write(commitDateTime)
outputFile.close()