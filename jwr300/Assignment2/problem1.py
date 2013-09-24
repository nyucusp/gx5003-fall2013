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
indexOfDate = 0
DateString = ""
tz = pytz.timezone('UTC')
targetDate = datetime.strptime(inputDate, "%m/%d/%Y %H:%M:%S") #user specified date
targetDate = targetDate.replace(tzinfo=tz)

#Read in the log data
myFile = open('logAfterAssignment1.txt','r')

for line in myFile:
			indexOfDate = line.find("Date:")
			if(indexOfDate != -1):
				DateString = line[indexOfDate:]
		        commitDate = dparser.parse(DateString,fuzzy=True)
		        commitDate = commitDate.replace(tzinfo=tz)
		        if commitDate > targetDate:
		            commitDateTimes.append(line)
	            	state = 0

myFile.close()


	            
#Output the result
print 'The date/times of the commits after ' + inputDate + ' were '
for commitDateTime in commitDateTimes:
    print commitDateTime


outputFile = open('output.txt','w')

for commitDateTime in commitDateTimes:
    outputFile.write(commitDateTime)
outputFile.close()