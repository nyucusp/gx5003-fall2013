from borough import Borough
from zipcode import Zipcode
import csv

boroughs = {}
boroughs = open('boroughs.csv','r')
zipborough = csv.reader(boroughs,delimiter= ',')

incidents = open('Incidents_grouped_by_Address_and_Zip.csv','r')
incident_brg = csv.reader(incidents,delimiter= ',')

population = open('zipCodes.csv','r')
populconsol = csv.reader(population,delimiter= ',')


def clean(list): # Inorder to clear the data
    checked = []
    for x in list:
       if x not in checked:
           checked.append(x)
    return checked


boroughs['Brooklyn'] = Borough('Brooklyn')
boroughs['Manhattan'] = Borough('Manhattan') 
boroughs['Bronx'] = Borough('Bronx')
boroughs['Staten'] = Borough('Staten')
boroughs['Queens'] = Borough('Queens')

for zip_1 in zipborough:    # clearing zipcodes
    zipcode = zip_1[0]
    for x in boroughs.b1():
        if zip_1[1]== x:
            boroughs[x].addZipcode(zipcode)

for x in boroughs.b1():
    boroughs[x].zipc = clean(boroughs[x].zipc)

    incident_brg.next()  # Incidents in each borough
for incident_1 in incident_brg:
    zipincid = incident_1[2]
    for x in boroughs.b1():
        for y in boroughs[x].zipc:
            if incident_1[1] == y:
                boroughs[x].addIncident(int(incident_1[2]))



populconsol.next()  # finding population in each borough
for pop_2 in populconsol:
    zip_2 = pop_2[10]
    if zip_2 !='':
        for x in boroughs.b1():
            for y in boroughs[x].zipc:
                if pop_2[1] == y:
                    boroughs[x].addPopulation(int(pop_2[10]))



outputFile = open('output_problem3.txt','w')  # Final output of the file
for x in sorted(boroughs.b1()):
    outputFile.write(x + ' '+ str(boroughs[x].incidents/float(boroughs[x].populations)) +'\n')
outputFile.close()
