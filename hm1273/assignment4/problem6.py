# Problem 6: Write SQL query to list set of zip codes in Manhattan along with their population where incidents have occurred. 

import sys
import MySQLdb
import csv


#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="hm1273", # your username
                   passwd="SQLuser", # your password
                   db="hmcoursedb") # name of the data base

# The Cursor object to execute the sql commands
cur = db.cursor() 

query = "select distinct borough, population from zipcodes JOIN Boroughs where borough = 'Manhattan' AND boroughs.zipcode = zipcodes.zipcode;"
cur.execute(query)

for row in cur.fetchall():
    print row[0], row[1]

db.close()
