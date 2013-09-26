#Aliya Merali
#Assignment 2
#Problem 1

import sys
import datetime
from dateutil import parser
logfile = open('log_assignment1.txt','r')

#Set the time limit to compare to from input value as an object in datetime
dateInput = sys.argv[1].split('/')
timeInput = sys.argv[2].split(':')
dateTimeLimit = datetime.datetime(int(dateInput[2]),int(dateInput[0]),int(dateInput[1]),int(timeInput[0]),int(timeInput[1]),int(timeInput[2]))
#I did this before I learned about the parser in dateutil

#Create a list with all the commit dates in it from the log file, then test for relationship to input time
for line in logfile:    
        indexOfDate = line.find("Date:")
        if (indexOfDate != -1):
            dateLine = parser.parse(line[6:32]) #Putting the Date line into an object in datetime (removing the beginning text 'Date' and end time zone
            if dateLine < dateTimeLimit: #comparing the two datetime objects
                pass 
            else:
                print line

