#Aliya Merali
#Assignment 2
#Problem 3

import csv
from collections import defaultdict

incident_log = open('Incidents_grouped_by_Address_and_Zip.csv','r')
borough_log = open('boroughs.csv','r')
zip_log = open('zipCodes.csv','r')
outputFile = open('output_problem3.txt','w')

#Creating a Dict with Zipcodes:No. Incidents in that Zipcode
#First, create a list of just zip codes
incidents = []
tempList = []
for line in incident_log.readlines():
    tempList = line.split(',')
    incidents.append(tempList[1][:5])
#next, create a dict with the zip key and no. of appearances as value
incidentByZip = defaultdict(int)
for x in range(len(incidents)):
    incidentByZip[incidents[x]] += 1 
#incidentByZip is the dict with {zip:#incidents}, assuming that each line in the input file represents only one incident

#Creating a Dictionary with Zipcodes:Borough Name
boroughDict = csv.DictReader(borough_log, ['ZipVal','BorName'])
boroughByZip = {}
for row in boroughDict:
    zipcode = row['ZipVal']
    boroughName = row['BorName']
    boroughByZip[zipcode] = boroughName 
#boroughByZip is the dict with {zip:BoroughName}

#Creating a Dictionary with ZipCodes:Population
zipDict = csv.DictReader(zip_log)
popByZip  = {} #Creating an empty dictionary for the zip:Pop dict
for row in zipDict: #filtering through the data dictionary
    if row['Total Population per ZIP Code'] != '': #if val for pop:
        zipcode = row['name']
        pop = row['Total Population per ZIP Code']
        popByZip[zipcode] = pop
#popByZip is the dict with {zip:totalPop}

#Creating the final dictionary
finalDict = {}
for zipKey in boroughByZip:
    tempPop = 0
    tempInc = 0
    if zipKey in popByZip:
        tempPop = popByZip[zipKey]
    if zipKey in incidentByZip:
        tempInc = incidentByZip[zipKey]
    if boroughByZip[zipKey] not in finalDict:
        finalDict[boroughByZip[zipKey]] = [0,0]
    finalDict[boroughByZip[zipKey]][1]+= int(tempPop)
    finalDict[boroughByZip[zipKey]][0]+= int(tempInc)

#Calculate and write the ratio of incidents to population
for keyVal in sorted(finalDict):
    ratio = float((finalDict[keyVal][0]))/float((finalDict[keyVal][1]))
    outputFile.write( str(keyVal) + ' ' + str(ratio)+ "\n")





