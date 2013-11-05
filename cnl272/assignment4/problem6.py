#Problem 6: List the set of zip codes in Manhattan along with their population where incidents have occurred.

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="cnl272",passwd="p00p00",db="coursedb")
cur=db.cursor()

query = "SELECT b.zip, z.population FROM boroughs b, zipcodes z WHERE b.zip = z.zip AND b.borough_name = 'Manhattan' AND b.zip in (SELECT i.zip from incidents i);" 
cur.execute(query)
for row in cur.fetchall():
	print row[0],row[1]

db.close()