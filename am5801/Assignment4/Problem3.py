# Awais Malik
# Assignment 4
# Problem 3
# Collaborated with Ender Faruk Morgul

import MySQLdb
import sys
import warnings

# Connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="am5801", # your username
                       passwd="12345", # your password
                       db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()

# User input
userboro = sys.argv[1]

warnings.filterwarnings('ignore', category=MySQLdb.Warning)

countincident="SELECT SUM(coursedb.incidents.uniquekey) FROM (SELECT DISTINCT coursedb.boroughs.zip \
from coursedb.boroughs WHERE coursedb.boroughs.bname='"+userboro+"') z, coursedb.incidents WHERE \
coursedb.incidents.zip=z.zip;"

cur.execute(countincident)

for row in cur.fetchall():
	if str(row[0])=='None':
		print "zip code cannot be found"
	else:
		count=row[0]

sumpopulation = "SELECT sum(i.population) FROM (SELECT DISTINCT \
coursedb.boroughs.zip from coursedb.boroughs WHERE coursedb.boroughs.bname='"+str(userboro)+"') z,\
coursedb.zipcodes i WHERE i.zip=z.zip;"

cur.execute(sumpopulation)

for row2 in cur.fetchall():
	if str(row2[0])=='None':
		print "zip code cannot be found"
	else:
		print "The ratio of the number of incidents to the population for the " + userboro + " borough is " + str(count/row2[0])

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()