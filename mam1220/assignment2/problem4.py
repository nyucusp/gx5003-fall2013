#!usr/bin/python

######################################################################
#
# 	Assignment 2 - Problem 4
# 	September 25th, 2013
#
# 	Michael Musick
#
#	Description: returns the avergae population of the user specified
#					borough	
#
#	Sample Input: python problem4.py "staten island"
#
######################################################################

# import zipcode
from borough import Borough
import sys
from string import lower

# get the user borough
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


# open the db file containing zipcodes for each borough
dbFile = open('boroughs.csv','r')

# create a Borough object
borough = Borough(userBorough)

# look through db file for zipcodes in that borough
for line in dbFile:
	tempArray = line.strip().split(',')
	zipnum = tempArray[0]
	
	# if its in the borough add it to the object
	if lower(tempArray[1]) == userBorough:
		borough.addZipcode( zipnum )

dbFile.close()

# open the next file and pull relevant pop and area information into borough object
dbFile = open('zipCodes.csv', 'r')
for line in dbFile:
	tempArray = line.strip().split(',')
	zipnum = tempArray[1]	

	# check that this is a zipcode in the user supplied borough
	if zipnum in borough.zipcodes:		
		# check that all values exist for that zip		
		# check that area is valid
		if len(tempArray[7]) > 0:		
			area = float( tempArray[7] )
		else:
			area = 0
		# check that the zip has a defined pop		
		if len(tempArray[10]) > 0:		
			pop = float( tempArray[10] )
		else:	# assign it to 0
			pop = 0

		# add the information to the object
		borough.modify_Pop_Area(zipnum, pop, area)
				
		# print "" + str(zipnum) + " " + str(area) + " " + str(pop) + " " 
dbFile.close()

# print the average population
print borough.avgPopStr()		