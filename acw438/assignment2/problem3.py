from zipcode import Zipcode
from borough import Borough

import csv

'''
Key assumptions: 
-"Unique Key" value in incidents csv is # of incidents.
-Including incidents from zips that don't have population, since calculation
is borough-wide.
'''

#zips with boroughs
borFileRaw = open('boroughs.csv', 'rU')
borFile = csv.reader(borFileRaw, delimiter=',')

#zips with population
popFileRaw = open('zipCodes.csv', 'r')
popFile = csv.DictReader(popFileRaw)

#zips with incidences
incidentFileRaw = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')
incidentFile = csv.DictReader(incidentFileRaw)


#add zips and populations to zipDict:
zipDict = {}
for popLine in popFile:
    zipDict[popLine['name']] = Zipcode('0',popLine['Total Population per ZIP Code'])

#add incidents (and zips that weren't in popFile) to zipDict:
for incident in incidentFile:
    incidentZip = incident['Incident Zip'][:5] #collapse 9-digit zips to 5-digit
    if incidentZip not in zipDict: #add zip to zipDict if it isn't there:
        zipDict[incidentZip] = Zipcode('0','')
    #then add number of incidents specified in Unique Key:
    zipDict[incidentZip].addIncident(incident['Unique Key'])

#compile incidents and zips into borDict:
borDict = {}
for zip in borFile:
    if zip[1] not in borDict: #add new boroughs
        borDict[zip[1]] = Borough(zip[1])
    if zip[0] in zipDict: 
        #add population and incidents only from available zips to
        #total population and total incidents in object
        borDict[zip[1]].addPopInst(zipDict[zip[0]].passAttributes())

outputFile = open('output_problem3.txt', 'w')

#sort borough dict and output results:
for borough in sorted(borDict.iterkeys()):
    #calculate final ratio, output
    outputLine = borough + " " + str(borDict[borough].calcIncdPopRatio()) + "\n"
    outputFile.write(outputLine)

outputFile.close()
borFileRaw.close()
popFileRaw.close()
incidentFileRaw.close()
