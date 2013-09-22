from zipcode import Zipcode
from borough import Borough

import csv

bFileRaw = open('boroughs.csv', 'rU')
boroughs = {}
zipcode = 0

bFile = csv.reader(bFileRaw, delimiter=',')
for line in bFile:
    if line[1] not in boroughs:
        boroughs[line[1]] = Borough(line[1])
    zipcode = Zipcode(line[0])
    boroughs[line[1]].addZipCode(zipcode)

for key in boroughs:
    curBor = boroughs[key].zipcodes
    print key + ":", ", ".join(x.number for x in curBor)

bFileRaw.close()
