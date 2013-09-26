#Kara Leary
#Urban Informatics
#Assignment 2 - Problem 3

import sys
import csv

#Initiate dictionaries of each borough's zip codes:
manhattanZipList = []
statenZipList = []
bronxZipList = []
queensZipList = []
brooklynZipList = []

#Initiate value for each borough's populations:
manhattanPop = 0
statenPop = 0
bronxPop = 0
queensPop = 0
brooklynPop = 0

#The function 'makeunique' will take the lists of the boroughs' zip
#codes and weed out any duplicate values so that I will be left with
#a dictionary with exactly one entry for each zip in an borough
def makeunique(list):
    found = []
    keep = []
    for entry in list:
        if entry not in found:
            found.append(entry)
            keep.append(entry)
    return keep


#This loop goes through the 'boroughs.csv' and append's each borough's
#zip code dictionary with the values found matching the name of the borough
with open('boroughs.csv') as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        if (row[1] == 'Manhattan'):
            tempZip = row[0]
            manhattanZipList.append(tempZip)
        elif (row[1] == 'Staten'):
            tempZip = row[0]
            statenZipList.append(tempZip)
        elif (row[1] == 'Bronx'):
            tempZip = row[0]
            bronxZipList.append(tempZip)
        elif (row[1] == 'Queens'):
            tempZip = row[0]
            queensZipList.append(tempZip)
        elif (row[1] == 'Brooklyn'):
            tempZip = row[0]
            brooklynZipList.append(tempZip)

#Here I employ the function defined above to weed out duplicate zip codes
manhattanZipList = makeunique(manhattanZipList)
statenZipList = makeunique(statenZipList)
bronxZipList = makeunique(bronxZipList)
queensZipList = makeunique(queensZipList)
brooklynZipList = makeunique(brooklynZipList)

#In this loop, I go through the 'zipCodes.csv' and compare the zip code in each
#entry to the existing dictionaries I have for each borough.  When a match is found,
#I access the population entry in that line and add it to the borough's population 
#count to get a final value of the population in that borough:
with open('zipCodes.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        if (row[10] != ''):  #Here, I ensure that the row has a value for population. Otherwise it is useless to me
            thisZip = row[1].strip()
            thisPop = float(row[10].strip())
            #Below, I go through each borough's zip code dictionary to see if the zip code in
            #'zipCodes.csv' is in that borough. If it is, I add the population value to that borough
            for line in manhattanZipList:
                if (thisZip == line):
                    manhattanPop += thisPop
            for line in statenZipList:
                if (thisZip == line):
                    statenPop += thisPop
            for line in bronxZipList:
                if (thisZip == line):
                    bronxPop += thisPop
            for line in queensZipList:
                if (thisZip == line):
                    queensPop += thisPop
            for line in brooklynZipList:
                if (thisZip == line):
                    brooklynPop += thisPop

#Initiate counts for the number of incidents in each borough:
manhattanIncidentCount = 0
statenIncidentCount = 0
bronxIncidentCount = 0
queensIncidentCount = 0
brooklynIncidentCount = 0

#In this loop, I read through the list of incidents and compare the zip code
#to the zip codes in each borough's dictionary.  If the zip codes match, I increment
#the number of incidents by one
with open('Incidents_grouped_by_Address_and_Zip.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        incidentZip = row[1]
        incidentZip = incidentZip[:5] #here, I truncate any entries that may be over 5 digits
        for line in manhattanZipList:
            if (incidentZip == line):
                manhattanIncidentCount += 1
        for line in statenZipList:
            if (incidentZip == line):
                statenIncidentCount += 1
        for line in bronxZipList:
            if (incidentZip == line):
                bronxIncidentCount += 1
        for line in queensZipList:
            if (incidentZip == line):
                queensIncidentCount += 1
        for line in brooklynZipList:
            if (incidentZip == line):
                brooklynIncidentCount += 1

manhattanRatio = manhattanIncidentCount/manhattanPop
statenRatio = statenIncidentCount/statenPop
bronxRatio = bronxIncidentCount/bronxPop
queensRatio = queensIncidentCount/queensPop
brooklynRatio = brooklynIncidentCount/brooklynPop

outputFile = open('output_problem3.txt', 'w')
outputFile.write('Bronx '), outputFile.write(str(bronxRatio)), outputFile.write('\n')
outputFile.write('Brooklyn '), outputFile.write(str(brooklynRatio)), outputFile.write('\n')
outputFile.write('Manhattan '), outputFile.write(str(manhattanRatio)), outputFile.write('\n')
outputFile.write('Queens '), outputFile.write(str(queensRatio)), outputFile.write('\n')
outputFile.write('Staten Island '), outputFile.write(str(statenRatio)), outputFile.write('\n')


outputFile.close()
