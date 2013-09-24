#!usr/bin/python

######################################################################
#
# tutorial 2 
# September 21th, 2013
#
######################################################################

import zipcode
import borough

boroughName = 'manhattan'

myFile = open('borough.cvs','r')

print myFile

lineNum = 0
for line in myFile:
	# indexOfBorough = line.find(boroughName)
	print line
	lineNum += 1
	print lineNum



# boroughs['manhattan'] = Borough('manhattan')

# zipcode = Zipcode(value_read_from_csv)
# boroughs['manhattan'].addZipcode(zipcode)


myFile.close()