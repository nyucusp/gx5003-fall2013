import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

cur.execute("(SELECT address FROM boroughs JOIN incidents WHERE nameBorough = 'Bronx' AND boroughs.zip = incidents.zip) UNION ALL (SELECT address FROM boroughs JOIN incidents WHERE nameBorough = 'Queens' AND boroughs.zip = incidents.zip);")

for row in cur.fetchall():
	print row[0]

db.close
