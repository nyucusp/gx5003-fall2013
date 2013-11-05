# Awais Malik
# Assignment 4
# Problem 2
# Collaborated with Ender Faruk Morgul

import MySQLdb
import sys

# Connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="am5801", # your username
                       passwd="12345", # your password
                       db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()

# User input
userzip = sys.argv[1]

query = "SELECT sum(a.population)/sum(a.area) FROM (SELECT coursedb.zipcodes.population, coursedb.zipcodes.area FROM coursedb.zipcodes WHERE coursedb.zipcodes.zip="+str(userzip)+") a;"

cur.execute(query)

for row in cur.fetchall():
	if str(row[0])=='None':
		print "This Zip Code could not be found. Sorry."
	else:
		print "The population density for the Zip code " + str(userzip) + " is: " + str(row[0])

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()