# Awais Malik
# Assignment 2
# Problem 4

import sys
import csv

zipFile = open('zipCodes.csv','r')
zipcodeList = csv.reader(zipFile)

boroughFile = open('boroughs.csv','r')
boroughList = csv.reader(boroughFile)

boroughName = sys.argv[1].lower()

zip = {}

for line in boroughList:
    zip[line[0]] = [line[1]]
       
for line in zipcodeList:
    if(line[0] in zip):
        zip[line[0]].append(line[10])

countManhattan = 0
countBrooklyn = 0
countBronx = 0
countQueens = 0
countStaten = 0

for line in zip:
    if(zip[line][0] == 'Manhattan'):
        countManhattan += 1
    elif(zip[line][0] == 'Brooklyn'):
        countBrooklyn += 1
    elif(zip[line][0] == 'Bronx'):
        countBronx += 1
    elif(zip[line][0] == 'Queens'):
        countQueens += 1
    elif(zip[line][0] == 'Staten'):
        countStaten += 1
    else:
        print "No Associated State!"

borough = {}

for line in zip:
    if(zip[line][0] not in borough):
        borough[zip[line][0]] = [0]
    try:
        borough[zip[line][0]][0] += int(zip[line][1])
    except:
        pass

if(boroughName == 'manhattan'):
    print float(borough['Manhattan'][0])/countManhattan
elif(boroughName == 'brooklyn'):
    print float(borough['Brooklyn'][0])/countBrooklyn
elif(boroughName == 'bronx'):
    print float(borough['Bronx'][0])/countBronx
elif(boroughName == 'queens'):
    print float(borough['Queens'][0])/countQueens
elif(boroughName == 'staten'):
    print float(borough['Staten'][0])/countStaten
else:
    print "Incorrect Entry!"