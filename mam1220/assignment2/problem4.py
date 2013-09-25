#!usr/bin/python

######################################################################
#
# Assignment 2 - Problem 4
# September 25th, 2013
#
# Michael Musick
#
#	Description: 	
#
#	Sample Input: python problem4 "staten island"
#
######################################################################

# import zipcode
from borough import Borough
from zipcode import Zipcode
import sys
from string import lower

userBorough = sys.argv[1]			# get the borough name
userBorough = lower(userBorough)	# convert it to lower case letters
if userBorough == "staten island":	# if its staten island convert
	userBorough = "staten"

# check that a valid borough was supplied
acceptableBoroughs = ['manhattan', 'brooklyn', 'queens', 'bronx', 'staten']
if userBorough not in acceptableBoroughs:
	print "ERROR: please enter a known borough"
	print acceptableBoroughs
	sys.exit()


dbFile = open('boroughs.csv','r')

borough = Borough(userBorough)

for line in dbFile:
	tempArray = line.strip().split(',')
	zipnum = tempArray[0]
	
	if lower(tempArray[1]) == userBorough:
		borough.addZipcode( zipnum )

dbFile.close()



dbFile = open('zipCodes.csv', 'r')


for line in dbFile:
	tempArray = line.strip().split(',')
	zipnum = tempArray[1]	

	# check that this is a zipcode in the user supplied borough
	if zipnum in borough.zipcodes:		
		# check that all values exist for that zip
		
		if len(tempArray[7]) > 0:		# check that area is valid
			area = float( tempArray[7] )
		else:
			area = 0
		if len(tempArray[10]) > 0:		# check that the zip has a defined pop	
			pop = float( tempArray[10] )
		else:	# assign it to 0
			pop = 0

		borough.modify_Pop_Area(zipnum, pop, area)
				
		# print "" + str(zipnum) + " " + str(area) + " " + str(pop) + " " 
dbFile.close()

print borough.avgPopStr()		