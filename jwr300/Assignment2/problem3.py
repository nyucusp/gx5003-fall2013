#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Problem 3

"""
Creating ZipCodes Population Dictionary with key as zipcode and value 
as the population of that zipcode
"""

Pop_File = open('zipCodes_tr.csv','r')
population_lines = []

for line in Pop_File:
    population_lines.append(line)
Pop_File.close()

zipCodes_header = population_lines[0].split(',') #adding column names to header

#strip the header of \n
zipCodes_header_length = len(zipCodes_header)
for i in range(0,zipCodes_header_length):
    zipCodes_header[i] = zipCodes_header[i].strip()

zipCodes_zip_index = zipCodes_header.index('zip code tabulation area')
zipCodes_population_index = zipCodes_header.index('Total Population per ZIP Code')

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

boroughs_zip_index = 0
boroughs_index = 1


boroughs_zipcode = {}

Borough_File_length = len(borough_lines)
for i in range(1, Borough_File_length):
    if borough_lines[i].split(',')[boroughs_index] != "\n":
        boroughs_zipcode[borough_lines[i].split(',')[boroughs_zip_index]] = (borough_lines[i].split(',')[boroughs_index].strip())


"""
Run through every key-value pair in zipCodes_population and add it to 
borough_zip_pop with key as borough and value as the borough population
"""
borough_zip_pop = {"Manhattan" : 0.0,"Brooklyn" : 0.0, "Queens": 0.0, "Bronx" : 0.0, "Staten" : 0.0}


for key in zipCodes_population:
    if boroughs_zipcode.has_key(key):
        borough_zip_pop[boroughs_zipcode[key].strip()] = borough_zip_pop[boroughs_zipcode[key].strip()] + zipCodes_population[key]




"""
Creating zipcode incidents dictionary with key as zipcode and value as 
incident count
"""
incidents_file = open('Incidents_grouped_by_Address_and_Zip.csv','r')

incidents_lines = []
for line in incidents_file:
    incidents_lines.append(line)

incidents_header = incidents_lines[0].split(',')

#strip the header of \n
incidents_header_length = len(incidents_header)
for i in range(0,incidents_header_length):
    incidents_header[i] = incidents_header[i].strip()

incidents_count_index = incidents_header.index('Unique Key')
incidents_zip_index = incidents_header.index('Incident Zip')

#Create a zip_incident dictionary (including dirty data)

incidents_length = len(incidents_lines)
    

incidents_zipcode = {} #create dictionary


for i in range(1,incidents_length):
    if (incidents_lines[i].split(',')[incidents_zip_index] != ''):
        if (incidents_zipcode.has_key(incidents_lines[i].split(',')[incidents_zip_index][0:5]) == False and boroughs_zipcode.has_key(incidents_lines[i].split(',')[incidents_zip_index][0:5])):
            incidents_zipcode[incidents_lines[i].split(',')[incidents_zip_index][0:5]] = int(incidents_lines[i].split(',')[incidents_count_index].strip())
        else:
            if (boroughs_zipcode.has_key(incidents_lines[i].split(',')[incidents_zip_index][0:5])):
                if (incidents_lines[i].split(',')[incidents_count_index] != ''):
                    incidents_zipcode[incidents_lines[i].split(',')[incidents_zip_index][0:5]] = incidents_zipcode[incidents_lines[i].split(',')[incidents_zip_index][0:5]] + int(incidents_lines[i].split(',')[incidents_count_index].strip())


"""
Create borough_incidents dictionary with key as borough name and value 
as incident count
"""
borough_incidents = {"Manhattan" : 0.0,"Brooklyn" : 0.0, "Queens": 0.0, "Bronx" : 0.0, "Staten" : 0.0}


for key in incidents_zipcode:
    if boroughs_zipcode.has_key(key):
        borough_incidents[boroughs_zipcode[key].strip()] = borough_incidents[boroughs_zipcode[key].strip()] + incidents_zipcode[key]
        
"""
Create borough_incidents dictionary with key as borough name and value 
as incident count density

"""
borough_incident_density = {"Manhattan" : 0.0,"Brooklyn" : 0.0, "Queens": 0.0, "Bronx" : 0.0, "Staten" : 0.0}

for key in borough_incident_density:
    borough_incident_density[key] = (borough_incidents[key] / borough_zip_pop[key])
    
#Update for full name of Staten Island
borough_incident_density["Staten Island"] = borough_incident_density["Staten"]
del borough_incident_density["Staten"]

#Output results of borough incident density dictionary to output txt file
outputFile = open('output_problem3.txt','w')

for key in sorted(borough_incident_density.iterkeys()):
    outputFile.write("%s %s \n" % (key, borough_incident_density[key]))

outputFile.close()