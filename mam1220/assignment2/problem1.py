#!usr/bin/python

######################################################################
#
# Assignment 2 - Problem 1 
# September 21th, 2013
#
# Michael Musick
#
#	Description: 	Returns the commits from gitlog that are newer than
#					the specified datetime
#	sample input:	python problem1.py "09/19/2013 09:12:15"
#
######################################################################

import sys
dateString = sys.argv[1]
# print dateString


from datetime import datetime
import time

# Convert to a dateObject
dateObject = time.strptime(dateString, "%m/%d/%Y %H:%M:%S")  
# print dateObject
# make that a datetime
refDate = datetime.fromtimestamp(time.mktime(dateObject))
# print refDate.strftime("%m/%d/%Y %H:%M:%S")


totalCommitsAfter = 0
findMessageLine = 3
logFile = open('logAfterAssignment1.txt', 'r')
for line in logFile:
	# print line
	indexOfDate = line.find("Date: ")
	if( indexOfDate != -1 ):		
		# Date:   Fri Sep 6 09:51:18 2013 -0400
		if( len(line) == 39 ):			
			lineDate = line[12:32]
		elif( len(line) == 38 ):
			lineDate = line[12:31]			
		# print lineDate
		dateObject = time.strptime(lineDate, "%b %d %H:%M:%S %Y")
		lineDate_  = datetime.fromtimestamp(time.mktime(dateObject))
		timeDiff = lineDate_ - refDate
		# print timeDiff
		# print timeDiff.total_seconds()
		# print ' '

		if( timeDiff.total_seconds() > 0 ):			
			print tempAuthLine + lineDate_.strftime("%m/%d/%Y %H:%M:%S")		
			print "Commit made " + str(timeDiff) + " after " + str(dateString)
			totalCommitsAfter += 1
			findMessageLine = 0

	# store the line incase its the author
	tempAuthLine = line
	
	#print next commit message after a date has been found
	if( findMessageLine < 3 ):
		if( findMessageLine == 2 ):
			print "Commit comment:" + line		
		findMessageLine += 1

print "Total number of commits after given date: " + str(totalCommitsAfter) + "\n"