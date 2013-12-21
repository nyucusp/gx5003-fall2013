# Problem 5: Write SQL query to list addresses of all incidents that have occurred either in Bronx or Queens. 


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

query = "select address from incidents where zipcode in (select zipcode from boroughs where borough = 'Bronx' or borough = 'Queens');"

cur.execute(query)

query_return = cur.fetchall()

for row in query_return:
    if row[0] != '':
        print row[0]

db.close()

