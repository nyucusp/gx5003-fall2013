import sys
import csv

currentZip = 0
currentPop = 0
currentArea = 0
populationDensity = 0

temparray = []

with open('zipCodes.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        if (row[10] != ''):
            currentZip = row[1].strip()
            currentPop = float(row[10].strip())
            currentArea = float(row[7].strip())
            populationDensity = currentPop/currentArea
            
            thisstring = currentZip, populationDensity
            temparray.append(thisstring)
            
            #print row[1].strip(), row[7].strip(), row[10].strip()

newarray = sorted(temparray)

#for entry in newarray:
#    print entry

#for line in newarray:
 #   outputFile.write(line)

#print temparray

#outputFile.close()

outputFile = open('output_density_problem2.txt', 'w')
for entry in newarray:
    outputFile.write(str(entry))
    outputFile.write('\n')
outputFile.close()
