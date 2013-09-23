#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 1
#Parses class github log file and compiles a list of commits after a user specified date


import pytz
import sys
from datetime import datetime
import dateutil.parser as dparser
inputDate = sys.argv[1]
commitDateTimes = []
state = 0
tz = pytz.timezone('UTC')
targetDate = datetime.strptime(inputDate, "%m/%d/%Y %H:%M:%S") #user specified date
targetDate = targetDate.replace(tzinfo=tz)

#Read in the log data
myFile = open('logAfterAssignment1.txt','r')

for line in myFile:
        #indexOfDate = line.find("Date:")
        commitDate = dparser.parse(indexOfDate,fuzzy=True)
        commitDate = commitDate.replace(tzinfo=tz)
        if commitDate > targetDate:
            commitDateTimes.append(line)
            
#Output the result
print 'The date/times of the commits after ' + inputDate + ' were '
for commitDateTime in commitDateTimes:
    print commitDateTime