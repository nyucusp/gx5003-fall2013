import sys
import MySQLdb

# take the user's input as input
input = sys.argv
zipGiven = input[0]

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

# define query to compute population density
query = "SELECT (population/area) FROM zipcodes WHERE zip = " + "'" + zipGiven + "'" + ";"
cur.execute(query)

for row in cur.fetchall():
	if len(cur.fetchall()) > 0:
		print "The population density in zipcode + 'sys.argv[0]' + " is " str(row[0])."
	else:
		print "'sys.argv[0]' + is not a New York zipcode." 

db.close()
