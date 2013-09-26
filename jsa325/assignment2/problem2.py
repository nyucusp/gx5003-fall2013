# input zipcodes and output population density by zip code

import sys

myFile = open('zipCodes.csv','r')
lines = []

for line in myFile:
  lines.append(line)
myFile.close()

header = lines[0].split(',') # split line 0 (first line) into header names
lengthHeader = len(header)
for i in range(0, lengthHeader):
    header[i] = header[i].strip()

indexZip = header.index('zip code') 
indexArea = header.index('area')
indexPopulation = header.index('population')

for line in lines:
  lineSplit = line.split(",")
  if lineSplit[10] != '\n': # test for blank
    lines.append([lineSplit[0], [lineSplit[7], [lineSPlit[10].rstrip()]])

zipPopulationDensity = {} # create dictionary

length = len(lines)

for i in range(1, length):
  if lines[i].split(',') != "\n":
    zipPopulationDensity[lines[i].split(',')[indexZip] = (float(lines[i].split(',')[indexPopulation].strip())/float(lines[i].split(',')[indexArea].strip())]
    
outputFile = open('outputDensity.txt', 'w')

for k in sorted(zipPopulationDensity):
  outputFile.write("%s %s \n" % (k, zipPopulationDensity[key]))
  
outputFile.close()
  
  
