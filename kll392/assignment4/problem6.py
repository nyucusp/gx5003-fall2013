#Kara Leary
#Urban Informatics - Assignment 4
#Problem 6

import MySQLdb

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

#I added "DISTINCT" so that a new entry would not be outputted each time an incident occurs in a zip code:
query = "SELECT DISTINCT B.zip, Z.population FROM zipcodes as Z, boroughs as B, incidents as I WHERE B.borough = 'Manhattan' and B.zip = Z.zip and B.zip = I.zip"

cur.execute(query)

for row in cur.fetchall():
    print row[0], row[1]

db.close()
