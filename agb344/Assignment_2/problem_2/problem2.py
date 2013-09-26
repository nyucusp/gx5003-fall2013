import csv

csvFile = open('zipCodes.csv','rb')
fileReader = csv.reader(csvFile)

fileReader.next() #Skip header line

zipDataTable = {} #Empty dictionary for zip code details
zipDensityTable = {}

outputFile = open('prob2_output.txt', 'w')
outputFile.write('zipcode density\n')

for row in fileReader:
    if row[10] != '':
        density = float(row[10])/float(row[7])
        outputFile.write(row[0]+" %f \n"%density)

