import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

cur.execute("SELECT address FROM boroughs JOIN incidents WHERE nameBorough = 'Manhattan' ANS boroughs.zip = incidents.zip;")

for row in cur.fetchall():
	print row[0]

db.commit()
db.close()
