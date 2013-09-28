import csv

incidentsFile = open('Incidents_grouped_by_Address_and_Zip.csv','rb')
boroughsFile = open('boroughs.csv','rb')
zipcodesFile = open('zipCodes.csv','rb')

boroughList = ['manhattan', 'queens', 'bronx', 'brooklyn', 'staten']

boroughDict = {'manhattan':[], 'queens':[], 'bronx':[], 'brooklyn':[], 'staten':[]}
incidentDict = {'manhattan':0, 'queens':0, 'bronx':0, 'brooklyn':0, 'staten':0}
populationDict = {'manhattan':0, 'queens':0, 'bronx':0, 'brooklyn':0, 'staten':0}

ratioDict = {'manhattan':0.0, 'queens':0.0, 'bronx':0.0, 'brooklyn':0.0, 'staten':0.0}


outputFile = open('output_problem3.txt', 'w')

def findBorough(zipcode):
    for b, z in boroughDict.iteritems():
        if zipcode in z:
            return b

for zipBorough in boroughsFile:
    thisZip = zipBorough.split(',')[0]
    thisBorough = zipBorough.split(',')[1]
    boroughDict[thisBorough.lower()[:-1]].append(thisZip)

for incident in incidentsFile:
    incidentZip = incident.split(',')[1]
    incidentBorough = findBorough(incidentZip)
    if incidentBorough in boroughList:
        incidentDict[incidentBorough] += 1

for zipcode in zipcodesFile:
    thisZip = zipcode.split(',')[1]
    thisPopulationString = zipcode.split(',')[10]
    if thisPopulationString[:-1].isdigit():
        thisPopulation = int(thisPopulationString)
        populationBorough = findBorough(thisZip)
        if populationBorough in boroughList:
            populationDict[populationBorough] += thisPopulation

for borough in ratioDict.keys():
    ratio = float(incidentDict[borough]) / float(populationDict[borough])
    ratioDict[borough] = ratio

sortedBoroughs = sorted(ratioDict.keys())

for borough in sortedBoroughs:
    outputFile.write(borough + '\t %f\n' %ratioDict[borough])

