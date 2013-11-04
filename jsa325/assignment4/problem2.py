import sys
import MySQLdb

# take the user's input as input
input = sys.argv
input.population(0)
zipGiven = input[0]

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")

cur = db.cursor()

# define query to compute population density
cur.execute("SELECT (population/area) FROM zipcodes WHERE zip = " + "'" + zipGiven + "'" + ";"

for row in cur.fetcha11():
	print row[0]

db.commit()
db.close()
