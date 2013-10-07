#problem3.py

#Compute ratio between number of incidents and the population of each borough
#output file "out_put.txt"
#alphabetical order

import sys
import csv
from collections import defaultdict

"""
bList = []
tempList = []
zipBoro = []
zipInc = []
zipPop = []


#function to read in file to list
def openRead(a):
    with open( a, 'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            tempList.append(line)
        return tempList


#read in the three files
zipBoro = openRead('boroughs.csv')
tempList = []
zipInc = openRead('Incidents_grouped_by_address_and_Zip.csv')
tempList = []
zipPop = openRead('zipCodes.csv')
tempList = []
"""

boro_by_zip = {}
boro_zips = defaultdict(list)
pop_by_boro = defaultdict(int)
incidents_by_boro = defaultdict(int)

# Read zipcode data.
for line in open('boroughs.csv').readlines():
    cols = line.strip().split(',')
    boro = cols[1].strip().lower()
    _zip = int(cols[0])

    boro_zips[boro].append(_zip)
    boro_by_zip[_zip] = boro

# Read population data.
lines = open('zipCodes.csv').readlines()
lines.pop(0)
for line in lines:
    cols = line.strip().split(',')

    if cols[1].isdigit() and cols[10]:
        _zip = int(cols[1])
        pop = int(cols[10])

        if _zip in boro_by_zip:
            boro = boro_by_zip[_zip]
            pop_by_boro[boro] += pop

#print pop_by_boro

# Read incidents data.
lines = open('Incidents_grouped_by_address_and_Zip.csv').readlines()
lines.pop(0)
for line in lines:
    cols = line.strip().rsplit(',', 2)

    if cols[1].isdigit():
        _zip = int(cols[1])
        incidents = int(cols[2])

        if _zip in boro_by_zip:
            boro = boro_by_zip[_zip]
            incidents_by_boro[boro] += incidents

#print incidents_by_boro

outFile = open("output_problem3.txt", "w")
for boro in boro_zips.keys():
    inc_per_capita = float(incidents_by_boro[boro]) / pop_by_boro[boro]
    print >> outFile, boro, inc_per_capita

outFile.close()

"""
class Borough():
    name = ""
    zipcodes = []
    pop = 0
    incid = 0
    i = 0
    boroName = ""
    n = 0
    #construct
    def __init__(self, name):
        self.name = name
        zipcodes = []
        #print name

    #Get all borough zip codes
    def getZipCode(self, name):
        i = 0
        zipcodes = []
        self.name = name
        #while index is less than length of list
        while i < len(zipBoro):
            #take associated with the zip code
            boroName = zipBoro[i]
            # compare the two names
            if name == boroName[1]:
                #set function zipcodes equal to the list of boro codes
                self.zipcodes = zipcodes.append(boroName[0])

            else:
                n=0
                #print name, boroName[1]
            i = i + 1
        return zipcodes

    #Add up all incidents in boro by zip code
    def getInc(self, zips):
        zipcodes = zips
        i = 0
        n = 0
        incid = 0
        tempZip = []
        zipInc.pop(0)
        tempList = []
        #while index is less than length of incident list
        while i < len(zipInc):
            tempZip = zipInc[i]
            #while index is less than length of zipcodes list
            n = 0
            while n < len(zipcodes):
                #if zip in incident list matches boro zip, then add the incidents to log


                while not tempZip[1]:
                    #print "STRING!"
                    i = i + 1
                    tempZip = zipInc[i]
                if tempZip[1] == "N/A" or tempZip[1] == "NY" or tempZip[1] == "NA":
                    #print "N/A!"
                    i = i + 1
                    tempZip = zipInc[i]
                while len(tempZip[1]) > 5:
                    #print "LongShort!"
                    i = i + 1
                    tempZip = zipInc[i]
                while len(tempZip[1]) < 5:
                    #print "LongShort!"
                    i = i + 1
                    tempZip = zipInc[i]

                    #This code below was originally meant to split a longer zip code
                    # tempList = tempZip[1].split("-", 1)
                    # tempZip[1] = tempList[0]
                    # tempList = []
                if int(tempZip[1]) == int(zipcodes[n]):
                    #print "here" #add incident to count
                    incid = incid + 1
                    n = n + 1
                else:

                    n = n + 1

            i = i + 1
        return incid

    #Add up all pop in boro by zip


#Manhattan Class
x = Borough("Manhattan")
bList = x.getZipCode("Manhattan")
z = x.getInc(bList)
print z

# #Brooklyn Class
# x = Borough("Brooklyn")
# bList = x.getZipCode("Brooklyn")
# x.getInc(bList)
"""
