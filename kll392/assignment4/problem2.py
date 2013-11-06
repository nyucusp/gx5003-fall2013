#Kara Leary
#Urban Informatics - Assignment 4
#Problem 2

import sys
import MySQLdb

zipCode = int(sys.argv[1])

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

query = "SELECT area, population FROM zipcodes WHERE zip =" + str(zipCode)
cur.execute(query)

#Grab values for area and population from query results:
for row in cur.fetchall():
    area = row[0]
    population = row[1]
    print population/area

db.close()
