import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

query = "SELECT (sum(population)) FROM boroughs JOIN zipcodes WHERE nameBorough = " + "'" + sys.argv[1] + "'" + "and boroughs.zip = zipcodes.zip;"
cur.execute(query)

for row in cur.fetchall():
	if len(cur.fetchall()) > 0:
		if row[0] == "Staten":
			print "The ratio of incidents to population in " + row[0] + " Island is " + str(row[1])
		else: 
			print "The ratio of incidents to population in " + row[0] + " is " + str(row[1])
	else: 
		print sys.argv[1] + " isn't a borough of New York City."

db.close()
