#Kara Leary
#Urban Informatics - Assignment 4
#Problem 5

import MySQLdb

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

query = "SELECT I.address, B.borough FROM incidents as I, boroughs as B WHERE (B.borough = 'Bronx' or B.borough = 'Queens') and I.zip = B.zip"

cur.execute(query)

for row in cur.fetchall():
    print row[0], row[1]

db.close()
