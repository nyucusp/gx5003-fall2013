#Kara Leary
#Urban Informatics - Assignment 4
#Problem 4

import MySQLdb

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

query = "SELECT address, B.borough FROM incidents as I, boroughs as B WHERE B.borough = 'Manhattan' and B.zip = I.zip;"
cur.execute(query)

#Print address and borough for incidents in Manhattan:
for row in cur.fetchall():
    print row[0], row[1]

db.close()






