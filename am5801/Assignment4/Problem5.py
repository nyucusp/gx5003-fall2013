# Awais Malik
# Assignment 4
# Problem 5
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

address_list = "SELECT coursedb.incidents.address from (select distinct coursedb.boroughs.zip from coursedb.boroughs where coursedb.boroughs.bname='Bronx' or 'Queens') s, \
coursedb.incidents WHERE coursedb.incidents.zip=s.zip"

cur.execute(address_list)

for row in cur.fetchall():
	print row[0]

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()