# Awais Malik
# Assignment 2
# Problem 2

import csv

myFile = open('zipCodes.csv','r')
myFilelist = csv.reader(myFile)

outputFile = open('output_density_problem2.txt','w')

output = []
density = 0

for line in myFilelist:
    tempzip = []
    if (line[0] != 'name' and line[10] != 'Total Population per ZIP Code' and line[10] != ''):
        tempzip.append(line[0])
        density = float(line[10])/float(line[7])
        tempzip.append(density)
        output.append(tempzip)

output.sort()

for line in output:
    temp = str(line[0]) + ' ' + str(line[1]) + '\n'    
    outputFile.write(temp)
outputFile.close()