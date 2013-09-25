#Kara Leary
#Urban Informatics
#Assignment 2 - Problem 2

import sys
import csv

#initialize variables for zip, population, area, density:
currentZip = 0
currentPop = 0
currentArea = 0
populationDensity = 0

#set up a temporary list to hold unsorted values
temparray = []

with open('zipCodes.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()   #skip the header row
    for row in rows:
        if (row[10] != ''):  #I used this to eliminate rows with no population entry
            currentZip = row[1].strip()
            currentPop = float(row[10].strip())
            currentArea = float(row[7].strip())
            populationDensity = currentPop/currentArea
            
            #create a string with the desired output values:
            thisstring = currentZip, populationDensity

            #add the current string to the unsorted list:
            temparray.append(thisstring)  

#sort the temporary list in lexicographical order
newarray = sorted(temparray)

outputFile = open('output_density_problem2.txt', 'w')
for entry in newarray:
    outputFile.write(str(entry))
    outputFile.write('\n')
outputFile.close()
