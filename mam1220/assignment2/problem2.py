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

# create a dictionary
zipDict = {}
# instantiate a lineCount Var
numOfLine = 0

# go through that freaking document
for line in dbFile:
	# print line
	numOfLine += 1
	# print numOfLine

	tempArray = line.strip().split(',')

	completeEntry = True

	# if the zip is valid
	if( tempArray[1].isdigit()):
		# print tempArray[1]		
		# print tempArray

		# check that each field has data
		if( len(tempArray[7]) > 0 ):
			area = float(tempArray[7])
		else:
			completeEntry = False

		if( len(tempArray[10]) > 0  ):
			pop = int(tempArray[10])
		else:
			completeEntry = False

		# if both fields were populated then enter that guy into the dict
		if( completeEntry ):			
			tempZipDict = {'area': area, 'population': pop }
			# print tempZipDict
			zipDict[int(tempArray[1])] = tempZipDict

# sort that sucker
sorted(zipDict)

# print that stuff out
outputFile = open('output_density_problem2.txt','w')
outputFile.write( "Zip Code\tPopulation Density\n")
for key in zipDict:
	tmpStr = str(key) + "\t\t" + str(zipDict[key]['population'] / zipDict[key]['area']) + "\n"
	outputFile.write(tmpStr)
# close the file
outputFile.close()
