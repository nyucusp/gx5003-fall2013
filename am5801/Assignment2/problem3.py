# Awais Malik
# Assignment 2
# Problem 3
# Main Assumption: Each address has ONE 311 incident.

import csv

zipFile = open('zipCodes.csv','r')
zipcodeList = csv.reader(zipFile)

boroughFile = open('boroughs.csv','r')
boroughList = csv.reader(boroughFile)

incidentFile = open('Incidents_grouped_by_Address_and_Zip.csv','rU')
incidentList = csv.reader(incidentFile)

outputFile = open('output_problem3.txt','w')
output = []

zip = {}

for line in boroughList:
    zip[line[0]] = [line[1]]
    zip[line[0]].append(0)

for line in incidentList:
    if(line[1] in zip):
        zip[line[1]][1] += 1
        
for line in zipcodeList:
    if(line[0] in zip):
        zip[line[0]].append(line[10])

borough = {}
for line in zip:
    if(zip[line][0] not in borough):
        borough[zip[line][0]] = [0,0]
    borough[zip[line][0]][1] += int(zip[line][1])
    try:
        borough[zip[line][0]][0] += int(zip[line][2])
    except:
        pass

for key in sorted(borough.iterkeys()):
    intensity = float(borough[key][1])/float(borough[key][0])
    tempy = key + ' ' + str(intensity) + '\n'
    outputFile.write(tempy)
outputFile.close()