# Awais Malik
# Assignment 2
# Tutorial 2
# tutorial2.py

from zipcode import Zipcode
from borough import Borough
import csv

myFile = open('boroughs.csv','r')
myFilelist = csv.reader(myFile)
boroughs = {}

for line in myFilelist:
    zipcode = Zipcode(line[0])
    if(line[1] in boroughs):    
        boroughs[line[1]].addZipcode(zipcode)
    else:
        boroughs[line[1]] = Borough(line[1])
        boroughs[line[1]].addZipcode(zipcode)

for line in boroughs:
    for entry in boroughs[line].zipcodes:
        print line, entry.number