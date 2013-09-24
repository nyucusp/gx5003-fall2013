#!usr/bin/python

######################################################################
#
# Assignment 2 - Problem 2 
# September 21th, 2013
#
# Michael Musick
#
#	Description: 	
#
######################################################################

dbFile = open('zipCodes.csv', 'r')

# name,zip code tabulation area,zt36 d00,perimeter,lsad trans,zt36 d00 i,lsad,area,latitude,longitude,Total Population per ZIP Code


numOfLine = 0
for line in dbFile:
	print line
	numOfLine += 1
	print numOfLine
