import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

query = "SELECT address FROM boroughs JOIN incidents WHERE nameBorough = 'Manhattan' AND boroughs.zip = incidents.zip;"
cur.execute(query)

for row in cur.fetchall():
	print row[0]

db.close()
