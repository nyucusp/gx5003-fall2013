from zipcode import Zipcode
from borough import Borough

import csv

bFileRaw = open('boroughs.csv', 'rU')
bFile = csv.reader(bFileRaw, delimiter=',')

boroughs = {}
zipcode = 0

for line in bFile:
    if line[1] not in boroughs:
        boroughs[line[1]] = Borough(line[1])
    zipcode = Zipcode(line[0])
    boroughs[line[1]].addZipCode(zipcode)

for key in boroughs:
    curBorZips = boroughs[key].zipcodes
    curBor = boroughs[key].name
    print curBor + ":", ", ".join(x.number for x in curBorZips)

bFileRaw.close()
