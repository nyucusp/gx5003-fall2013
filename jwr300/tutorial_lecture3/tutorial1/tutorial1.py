#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Tutorial for Assignment 2 that looks for a github collaborator
# and outputs a list of date/times of commits


import sys
myFile = open('//Volumes/250GB HDD/Users/Shared/Code/NYU/gx5003-fall2013/jwr300/tutorial_lecture3/tutorial1/logsofar.txt','r')
collabName = sys.argv[1]
state = 0
commitDateTimes = []
for line in myFile:
    if(state == 0): #look for author line
        indexOfCollab = line.find(collabName)
        if(indexOfCollab != -1): #found a commit from Collab
            state = 1 #now find the date time of this commit
        else:
            indexOfDate = line.find("Date:")
            if(indexOfDate != -1): #found date from the preview commit
                commitDateTimes.append(line)
                state = 0
myFile.close()

#Output the result
#print 'The date/times of the commits of ' + collabName + ' were '
#for commitDateTime in commitDateTimes:
#    print commitDateTime

outputFile = open('/Volumes/250GB HDD/Users/Shared/Code/NYU/gx5003-fall2013/jwr300/tutorial_lecture3/tutorial1/output.txt','w')

for commitDateTime in commitDateTimes:
    outputFile.write(commitDateTime)
outputFile.close()