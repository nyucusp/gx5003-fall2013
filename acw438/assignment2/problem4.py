from zipcode import Zipcode
from borough import Borough

import csv
import sys

#get borough from command line
borKey = sys.argv[1]
#put in title case to match dataset
borKey = borKey.title()

#borough file
bFileRaw = open('boroughs.csv', 'rU')
bFile = csv.reader(bFileRaw, delimiter=',')

#zip file
zipsRaw = open('zipCodes.csv', 'r')
zips = csv.DictReader(zipsRaw)

boroughs = {}
zipcode = 0
zipDict = {}

#iterate through zips in zipcodes.csv
for line in zips:
    if line['Total Population per ZIP Code'] != '':
        #add zipcode only if it has population data
        zipDict[line['name']] = line['Total Population per ZIP Code']

#iterate through zips in boroughs
for line in bFile:
    if line[1] not in boroughs:
        boroughs[line[1]] = Borough(line[1]) #add new boroughs
    if line[0] in zipDict: #If we don't have pop for zip, don't bother
        zipPop = zipDict[line[0]] #make population variable
        zipcode = Zipcode(line[0], zipPop) #make zipcode object
        #add zipcode object to zipcode list in borough obj
        boroughs[line[1]].addZipCode(zipcode)
        zipDict[line[0]] = 0 #set population of zip to zero to avoid duplicates

try:
    print boroughs[borKey].avgZipPop() #calculate pop/zip average.
except:
    print "No such borough."

bFileRaw.close()
zipsRaw.close()
