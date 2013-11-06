#Kara Leary
#Urban Informatics  - Assignment 4
#Problem 3

import MySQLdb
import sys
import decimal

Borough = sys.argv[1]
#Make input borough lower case so that it will always match entries in table:
borough = Borough.lower()

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

#Query #1: grab all zip codes for the inputted borough
zipQuery = "SELECT zip FROM boroughs WHERE borough =" + "'" + str(borough) + "';"
cur.execute(zipQuery)

#Create list of zip codes for given borough:
zipCodes = []
for row in cur.fetchall():
    zipCodes.append(row[0])

#Query each individual zipcode in zipcode list, add population to running count of total population for that borough:
population = 0
for entry in zipCodes:
    popQuery = "SELECT zip, population FROM zipcodes WHERE zip =" + str(entry) + ";"
    cur.execute(popQuery)
    for row in cur.fetchall():
        population += row[1]

#Query each individual zipcode in zipcode list, increment incident count by one each time an entry matches a zipcode in the inputted borough:
incidentTotal = 0
for entry in zipCodes:
    incidentQuery = "SELECT incidentID, zip FROM incidents WHERE zip=" + str(entry) + ";"
    cur.execute(incidentQuery)
    for row in cur.fetchall():
        incidentTotal += 1

#Compute ratio:
ratio = float(incidentTotal)/float(population)

print "The ratio between incidents and population in ", borough, " is ", ratio

db.close()
