import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

cur.execute("SELECT intermediate.zip, population FROM (SELECT distinct incidents.zip FROM boroughs JOIN incidents WHERE nameBorough = 'Manhattan' AND boroughs.zip = incidents.zip) AS intermediate JOIN zipcodes WHERE intermediate.zip = zipcodes.zip;")

for row in cur.fetchall():
	print row[0], row[1]

db.commit()
db.close()
