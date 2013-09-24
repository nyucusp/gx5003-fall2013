from zipcode import Zipcode
from borough import Borough

import csv
import sys

borKey = sys.argv[1]
borKey = borKey.title()

bFileRaw = open('boroughs.csv', 'rU')
bFile = csv.reader(bFileRaw, delimiter=',')

zipsRaw = open('zipCodes.csv', 'r')
zips = csv.DictReader(zipsRaw)

boroughs = {}
zipcode = 0
zipDict = {}

for line in zips:
    if line['Total Population per ZIP Code'] != '':
        zipDict[line['name']] = line['Total Population per ZIP Code']

for line in bFile:
    if line[1] not in boroughs:
        boroughs[line[1]] = Borough(line[1])
    if line[0] in zipDict: #If we don't have pop for zip, don't include in calc
        zipPop = zipDict[line[0]]
        zipcode = Zipcode(line[0], zipPop)
        boroughs[line[1]].addZipCode(zipcode)

try:
    print boroughs[borKey].avgZipPop()
except:
    print "No such borough."

bFileRaw.close()
zipsRaw.close()
