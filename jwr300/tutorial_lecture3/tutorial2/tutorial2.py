#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Tutorial 2
#

from borough import Borough
from zipcode import Zipcode
import csv


myFile = open('boroughs.csv', 'rU')
File = csv.reader(myFile, delimiter=',')

borough_list = {}
zipcode = 0

for line in File:
	if line[1] not in borough_list:
		borough_list[line[1]] = Borough(line[1])
	zipcode = Zipcode(line[0])
	borough_list[line[1]].addZipcode(zipcode)

print borough_list




#boroughs['manhattan'] = Borough('manhattan')
#zipcode = Zipcode(value_read_from_csv)
#boroughs['manhattan'].addZipcode(zipcode)