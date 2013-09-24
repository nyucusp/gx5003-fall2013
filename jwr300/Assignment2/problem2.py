#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 2
#Calculates the population density by zipcode for NY State


import csv
from collections import defaultdict

myFile = open('zipCodes.csv','rU')
File = csv.reader(myFile)
rows = []


#Adding csv to list for easy indexing 
for row in File:
    rows.append(row)

myFile.close()
    
header = rows[0] #adding column names to header
zip_index = header.index('zip code tabulation area')
area_index = header.index('area')
population_index = header.index('Total Population per ZIP Code')

#create a set of unique zip codes
zipDict = set()
for row in rows:
    zipDict.add(row[zip_index])

#convert unique zip codes back to list
zipDict = list(zipDict)

#create dictionary of key value pairs of area and zip code
#create dictionary of key value pairs of population and zip code

zipArea = defaultdict(list)
zipPop = defaultdict(list)
for zipcode in zipDict:
    for row in rows:
        if (zipcode == row[zip_index]):
            zipArea.setdefault(zipcode, []).append(row[area_index])
            if (row[population_index] != ''): #pop column has some blank cells
                zipPop.setdefault(zipcode, []).append(row[population_index])


zipPopDensity = {}
sumArea = 0.0
sumPop = 0.0
for zipcode in zipDict:
    sumAreaList = zipArea[zipcode]
    #float_list = [float(i) for i in sumAreaList]
    for item in sumAreaList:
        sumArea = sumArea + float(item)
    sumPopList = zipPop[zipcode]
    float_poplist = [float(i) for i in sumPopList]
    for item in float_poplist:
        sumPop = sumPop + item
    zipPopDensity[zipcode] = (sumPop/sumArea)

outputFile = open('output_problem2.txt','w')

for item in zipPopDensity:
    outputFile.write(item)

outputFile.close()
