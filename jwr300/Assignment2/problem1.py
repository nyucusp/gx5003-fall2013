#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 1
#Parses class github log file and compiles a list of commits after a user specified date


import sys
from datetime import datetime



#Read in the log data
myFile = open('logAfterAssignment1.txt','r')


date = datetime.strptime(sys.argv[1], "%m/%d/%Y %H:%M:%S") #user specified date
print date
