import sys
import borough as boroughClass
import zipcode as zipClass

Manhattan = boroughClass.Borough('Manhattan')
Brooklyn = boroughClass.Borough('Brooklyn')
Queens = boroughClass.Borough('Queens')
Staten = boroughClass.Borough('Staten Island')
Bronx = boroughClass.Borough('Bronx')

boroughDict = {'manhattan':Manhattan, 'brooklyn':Brooklyn, 'queens':Queens, 'staten':Staten, 'bronx':Bronx}
boroughList = {'manhattan':[], 'brooklyn':[], 'queens':[], 'staten':[], 'bronx':[]}
zipcodesFile = open('zipCodes.csv','rb')
boroughsFile = open('boroughs.csv','rb')

searchBorough = sys.argv[1]

def findBorough(zipcode):
    for b, z in boroughList.iteritems():
        if zipcode in z:
            #print b
            return b


for zipBorough in boroughsFile:
    thisZip = zipBorough.split(',')[0]
    thisBorough = zipBorough.split(',')[1]
    boroughList[thisBorough.lower()[:-1]].append(thisZip)

for zipcode in zipcodesFile:
    thisZip = zipcode.split(',')[1]
    thisAreaString = zipcode.split(',')[7]
    thisPopulationString = zipcode.split(',')[10]
    if thisPopulationString[:-1].isdigit():
        thisPopulation = float(thisPopulationString)
        thisArea = float(thisAreaString)
        populationBorough = findBorough(thisZip)
        if populationBorough in boroughDict.keys():
            thisZipcode = zipClass.Zipcode(thisZip, thisPopulation, thisArea)
            boroughDict[populationBorough].addZipcode(thisZipcode)
            
for borough in boroughDict.keys():
    if searchBorough == boroughDict[borough].name.lower():
        print boroughDict[borough].getAvgPopulation()
