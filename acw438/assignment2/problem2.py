#Alex Chohlas-Wood (acw438). Assignment 2, Problem 2.

'''
Key assumption: if I find duplicate zipcode entries in zipcodes.csv,
I will average out values for area and population for those 
duplicates and return the average population density at the end. 
'''

import csv
from zipcode import Zipcode

#open csv with universal newline support
zipFileRaw = open('zipcodes.csv', 'rU')
#parse the csv into a collection of dictionaries
zipFile = csv.DictReader(zipFileRaw, delimiter=',')

zipAreas = {}

for line in zipFile:
    popl = line['Total Population per ZIP Code']
    if popl != '': #filter out empty population lines
        popl = float(popl) #float because we may need to avg this value
    area = float(line['area'])
    if line['name'] not in zipAreas: 
        #zipcodes that haven't been found yet
        zipAreas[line['name']] = Zipcode(line['name'], popl, area)
    else:
        #average data from multiple zipcode entries
        zipAreas[line['name']].avgFeatures(popl, area)

outputFile = open("output_density_problem2.txt", 'w')

#sort the dict by keys, then output to file:
for zips in sorted(zipAreas.iterkeys()):
    if zipAreas[zips].population != 0:
        outputLine = zips + " " + str(zipAreas[zips].densityCalc()) + "\n"
        outputFile.write(outputLine)

outputFile.close()
zipFileRaw.close()
