#Katherine Elliott
#ke638
#Assignment 2 Problem 1

import sys
from datetime import datetime
import dateutil.parser as dparser

rawtime = sys.argv[1]
rawtime += ' -0400'#gives time zone
truetime = dparser.parse(rawtime, fuzzy =True) #parses argument to compile commits to accept different formats
commitDateTimes = []
state = 0
indexOfDate = 0
DateString = ""

myFile = open('logAfterAssignment1.txt','r') #runs file
for line in myFile:
    indexOfDate = line.find("Date:")
    if(indexOfDate != -1):
        DateString = line[indexOfDate:]
        commitDate = dparser.parse(DateString, fuzzy =True)    
        if commitDate > truetime:
            commitDateTimes.append(line)
            state = 0

myFile.close()    

#Output
print 'The date/times of the commits after ' + rawtime + ' were '
for commitDateTime in commitDateTimes:
    print commitDateTime

outputFile = open('output.txt','w')

for commitDateTime in commitDateTimes:
    outputFile.write(commitDateTime)
outputFile.close()
        