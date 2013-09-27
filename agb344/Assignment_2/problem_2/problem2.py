import csv

csvFile = open('zipCodes.csv','rb')
fileReader = csv.reader(csvFile)

fileReader.next() #Skip header line

zipDataTable = {} #Empty dictionary for zip code details
zipDensityTable = {}

outputFile = open('prob2_output.txt', 'w')

for row in fileReader:
    zipcodeString = row[0]
    areaString = row[7]
    populationString = row[10]
    if populationString != '':
        density = float(populationString)/float(areaString)
        zipDensityTable[zipcodeString] = density

sortedZipCodes = sorted(zipDensityTable.keys())

for k in sortedZipCodes:
    outputFile.write(k+'\t%f\n' %zipDensityTable[k])
