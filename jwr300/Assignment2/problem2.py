#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 2
"""
Calculates the population density by zipcode for NY State. 
This assumes there is only one unique record for each zipcode and ignores 
dirty data that is included in the underlying CSV which contains duplicates
for a handful of zipcodes 
"""

import sys


myFile = open('zipCodes.csv','r')
lines = []

#Adding csv to list
for line in myFile:
    lines.append(line)
myFile.close()
    
#store column headers and get index values for relevant columns required for calculation
header = lines[0].split(',') 
zip_index = header.index('zip code tabulation area') 
area_index = header.index('area')
population_index = header.index('Total Population per ZIP Code\n')

#create a dictionary of zipcodes-population density key value pairs
zipPopdensity = {}

length = len(lines)

for i in range(1,length):
    if lines[i].split(',')[10] != "\n":
        zipPopdensity[lines[i].split(',')[zip_index]] = (float(lines[i].split(',')[population_index].strip())/float(lines[i].split(',')[area_index].strip()))
                                                      
outputFile = open('output_density_problem2.txt','w')

for key in sorted(zipPopdensity.iterkeys()):
    outputFile.write("%s %s \n" % (key, zipPopdensity[key]))

outputFile.close()