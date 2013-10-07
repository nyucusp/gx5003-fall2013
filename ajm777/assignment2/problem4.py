#Aliya Merali
#Assignment 2
#Problem 4

import sys
import csv
from borough import Borough
borInput = sys.argv[1]
borInput = borInput.title()
boroughZipRef = open('boroughs.csv','r')
zipPopRef = open('zipCodes.csv','r')

#Set the input borough as an instance of the class Borough
borObj = Borough(borInput)

#Add to the list of zip codes in the borough class using the method addZipcode
boroughDict = csv.DictReader(boroughZipRef, ['ZipVal','BorName'])
for row in boroughDict:
    if row['BorName'] == borInput:
        borObj.addZipcode(row['ZipVal'])

#Sum the population in the zips of the borough by comparing zipcode values from the file to the zipcodes list in boroughs
popBorInput = csv.DictReader(zipPopRef)
totPopBor = 0
count = 0
for row in popBorInput: 
    if row['Total Population per ZIP Code'] != '': 
        pop = row['Total Population per ZIP Code']
        zipcode = row['name']
        if zipcode in borObj.zipcodes:
            count = count + 1
            totPopBor = totPopBor + int(pop)
           
#Calculate Average through the method in the borough class
borObj.calcAvgPop(totPopBor, count)

print borObj.avg

