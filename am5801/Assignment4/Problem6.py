# Awais Malik
# Assignment 4
# Problem 6
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

selection = "SELECT a.zip, a.population FROM (SELECT DISTINCT i.zip from (SELECT DISTINCT coursedb.boroughs.zip \
from coursedb.boroughs WHERE coursedb.boroughs.bname='Manhattan') z, coursedb.incidents i \
WHERE z.zip = i.zip) s, coursedb.zipcodes a WHERE s.zip=a.zip and a.population is not null"

cur.execute(selection)

for row in cur.fetchall():
	print row[0] + " " + row[1]

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()