import csv
import MySQLdb
import sys

#connect to database
db = MySQLdb.connect(host='localhost',
    user='ak4706',
    passwd='Atara7890',
    db = 'coursedb')
cursor = db.cursor()
zipinput = str(sys.argv[1])

#query to get the area and population for the given zipcode
query = "SELECT area, pop FROM Zipcode WHERE Zip=%s"
cursor.execute(query, zipinput)

#get the population density
for row in cursor.fetchall():
	popdens=float(row[1])/float(row[0])
	print "The population density for zipcode " + str(zipinput) + " is " + str(popdens)

db.close()