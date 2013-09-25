#!usr/bin/python

######################################################################
#
# tutorial 2 
# September 21th, 2013
#
######################################################################

# import zipcode
from borough import Borough
from zipcode import Zipcode

myFile = open('boroughs.csv','r')

# print myFile

boroughs = {}
lineNum = 0
for line in myFile:
	# indexOfBorough = line.find(boroughName)
	# print line
	lineNum += 1
	# print lineNum
	tempArray = line.strip().split(',')

	boroughName = tempArray[1]
	lineZip = int( tempArray[0] )

	if boroughName not in boroughs:
		boroughs[boroughName] = Borough(boroughName)
		# print boroughs[boroughName]

	if lineZip not in boroughs[boroughName].zipcodes:
		boroughs[boroughName].addZipcode(lineZip)
		# print boroughs[boroughName].zipcodes





# zipcode = Zipcode(value_read_from_csv)
# boroughs['manhattan'].addZipcode(zipcode)


myFile.close()