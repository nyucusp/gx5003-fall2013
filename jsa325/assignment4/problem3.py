import sys
import MySQL db

input = sys.argv
boroughGiven = input[0].split()[0]

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb"

cur = db.cursor()

cur.execute(SELECT sum(population) FROM boroughs JOIN zipcodes WHERE nameBorough = " + "'" + boroughGiven + "'" + "and boroughs.zip = zipcodes.zip;"

for row in cur.fetchall():
	if len(cur.fetchall()) > 0:
		if row[0] == "Staten":
			print "The ratio of incidents to population in " + row[0] + " Island is " + str(row[1])
		else: 
			print "The ratio of incidents to population in " + row[0] + " is " + str(row[1])
	else: 
		print sys.argv[0] + " isn't a borough of New York City."

db.commit()
db.close()
