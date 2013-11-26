import csv
import sys
import MySQLdb

#connect to database
db = MySQLdb.connect(host='localhost',
    user='ak4706',
    passwd='Atara7890',
    db = 'coursedb')

cursor = db.cursor()

#query to get the zipcode and population from Zipcode file whose zips are in Manhattan and in the incident file(an incident happened there)
query = "SELECT Zipcode.Zip, pop FROM Zipcode WHERE Zipcode.Zip IN (SELECT Borough.Zip FROM Borough WHERE Borough = 'Manhattan' and Borough.Zip IN(SELECT Inczip FROM Incidents))"
cursor.execute(query)

for row in cursor.fetchall():
	print "For Zipcode " + str(row[0]) + " in Manhattan where an incident has occured, the population is " + str(row[1])

db.close()