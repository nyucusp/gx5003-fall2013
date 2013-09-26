#!usr/bin/python

######################################################################
#
# Assignment 2 - Problem 3
# September 21th, 2013
#
# Michael Musick
#
#	Description: 	
#
######################################################################

dbFile = open('zipCodes.csv', 'r')


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

	# if the zip is valid
	if( tempArray[1].isdigit()):
		# print tempArray[1]		
		# print tempArray

		# this is the population for a given zip
		if( len(tempArray[10]) > 0  ):
			pop = int(tempArray[10])
		else:
			completeEntry = False

		tempZipDict = {'population': pop, 'incidents': 0 }
		# print tempZipDict
		zipDict[int(tempArray[1])] = tempZipDict

# sort that sucker
sorted(zipDict)
# close it up
dbFile.close();

dbFile = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')

numOfLine = 0
for line in dbFile:
	numOfLine += 1
	tempArray = line.strip().split(',')

	# get the zip key
	if( tempArray[1].isdigit() ):
		key = int(tempArray[1])
		# add one to an incident report or create a zip if it does not exist
		if key in zipDict:
			zipDict[key]['incidents'] += 1
		else:
			zipDict[key] = {'population': 0, 'incidents': 0 }

dbFile.close()
# print zipDict

dbFile = open('boroughs.csv', 'r')

boroughDict = {}
numOfLine = 0
for line in dbFile:
	numOfLine += 1

	tempArray = line.strip().split(',')
	

	borough = tempArray[1]
	if borough in boroughDict:
		boroughDict[borough]['zips'].append(int(tempArray[0]))
	else:
		zips = [int(tempArray[0])]
		boroughDict[borough] = {'zips': zips}
dbFile.close()

sorted(boroughDict)


# open up the output file
writeFile = open('output_problem3.txt', 'w')
writeFile.write('Number of incidents per person for each borough of NYC\n\n')
writeFile.write('Borough\t\tRatio Of Incidents\n\n')

# make sure they are sorted
for borough in boroughDict:	
	sorted(boroughDict[borough]['zips'])

	borPop = 0
	borInc = 0

	for zips in boroughDict[borough]['zips']:
		if zips in zipDict:
			borPop += zipDict[zips]['population']
			borInc += zipDict[zips]['incidents']

	# print "" + str(borough) + " " + str(borPop) + " " + str(borInc)

	incidentRatio = float(borInc) / float(borPop)
	if( len(borough) > 6 ):		
		borStr = "" + str(borough) + "\t" + str(incidentRatio) + "\n"
	else:
		borStr = "" + str(borough) + "\t\t" + str(incidentRatio) + "\n"

	writeFile.write(borStr)

# close that up
writeFile.close()

