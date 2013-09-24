from zipcode import Zipcode
from borough import Borough

import csv

#zips with boroughs
borFileRaw = open('boroughs.csv', 'rU')
borFile = csv.reader(borFileRaw, delimiter=',')

#zips with population
popFileRaw = open('zipCodes.csv', 'r')
popFile = csv.DictReader(popFileRaw)

#zips with incidences
incidentFileRaw = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')
incidentFile = csv.DictReader(incidentFileRaw)


#add zips and populations to zipDict
zipDict = {}
for popLine in popFile:
    zipDict[popLine['name']] = Zipcode('0',popLine['Total Population per ZIP Code'])

#add incidents (and some more zips) to zipDict
for incident in incidentFile:
    incidentZip = incident['Incident Zip'][:5]
    if incidentZip in zipDict:
        zipDict[incidentZip].addIncident()
    else:
        zipDict[incidentZip] = Zipcode('0','')
        zipDict[incidentZip].addIncident()

#compile incidents and zips into borDict:
borDict = {}
for zip in borFile:
    if zip[1] not in borDict:
        borDict[zip[1]] = Borough(zip[1])
    if zip[0] in zipDict:
        borDict[zip[1]].addPopInst(zipDict[zip[0]].passAttributes())

outputFile = open('output_problem3.txt', 'w')

for borough in sorted(borDict.iterkeys()):
    outputLine = borough + " " + str(borDict[borough].calcInstPopAvg()) + "\n"
    outputFile.write(outputLine)

outputFile.close()
borFileRaw.close()
popFileRaw.close()
incidentFileRaw.close()
