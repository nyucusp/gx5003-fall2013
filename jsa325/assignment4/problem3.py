import sys
import MySQL db

input = sys.argv
boroughGiven = input[0].split()[0]

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb"

cur = db.cursor()

cur.execute(SELECT sum(population) FROM boroughs JOIN zipcodes WHERE nameBorough = " + "'" + boroughGiven + "'" + "and boroughs.zip = zipcodes.zip;"

for row in cur.fetchall():
	print "The ratio of incidents to population in " + row[0] + " is " + str(row[0])

db.commit()
db.close()
