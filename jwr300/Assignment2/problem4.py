#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 4

import sys
import borough
import zipcode

"""
Adjusts the input from "staten island" to "Staten" given the form
of the underlying data in boroughs.csv
"""
if sys.argv[1] == "staten island":
	borough_input = "Staten"
else:
	borough_input = sys.argv[1].capitalize()


"""
Creating ZipCodes Population Dictionary with key as zipcode and value 
as the population of that zipcode
"""
Pop_File = open('zipCodes_tr.csv','r')
population_lines = []

for line in Pop_File:
    population_lines.append(line)
Pop_File.close()

zipCodes_header = population_lines[0].split(',') #adding column names to header variable
zipCodes_zip_index = zipCodes_header.index('zip code tabulation area')
zipCodes_population_index = zipCodes_header.index('Total Population per ZIP Code\n')

zipCodes_population = {}

Pop_File_length = len(population_lines)

for i in range(1,Pop_File_length):
    if population_lines[i].split(',')[10] != "\n":
        zipCodes_population[population_lines[i].split(',')[zipCodes_zip_index]] = (float(population_lines[i].split(',')[zipCodes_population_index].strip()))


"""
Creating zipcode Borough dictionary with key as zipcode and value as 
borough names
"""
Borough_File = open('boroughs_tr.csv','r')
borough_lines = []

for line in Borough_File:
    borough_lines.append(line)
Borough_File.close()

#Setting column names to index variables 
boroughs_zip_index = 0
boroughs_index = 1

boroughs_zipcode = {}

Borough_File_length = len(borough_lines)
for i in range(1, Borough_File_length):
    if borough_lines[i].split(',')[boroughs_index] != "\n":
        boroughs_zipcode[borough_lines[i].split(',')[boroughs_zip_index]] = (borough_lines[i].split(',')[boroughs_index].strip())

borough_zip_pop = {"Manhattan" : 0.0,"Brooklyn" : 0.0, "Queens": 0.0, "Bronx" : 0.0, "Staten" : 0.0}

"""
Run through every key-value pair in zipCodes_population and add it to borough_zip_pop with the key 
being the borough and the value containing the borough population

"""

for key in zipCodes_population:
    if boroughs_zipcode.has_key(key):
        borough_zip_pop[boroughs_zipcode[key].strip()] = borough_zip_pop[boroughs_zipcode[key].strip()] + zipCodes_population[key]

#Create Borough object 
userBorough = borough.Borough(borough_input)


"""
Cycles through zipcodes and associated population and creates zipcode objects.
The zipcode objects are then added to the borough object.
"""
for key in boroughs_zipcode:
	if boroughs_zipcode[key] == borough_input:
		if key in zipCodes_population:
			zip_code = zipcode.Zipcode(key, zipCodes_population[key])
			userBorough.addZipcode(zip_code)

"""
Calling the aveverage population method to calculate the average zip population 
and return the value for the user specified borough
"""
average = userBorough.averagePopulation()
print average





