import MySQLdb
import sys
from decimal import *
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="ak4728", # your username
                   passwd="password", # your password
                   db="coursedb") # name of the data base  
# The Cursor object will let you execute the sql commands
cur = db.cursor()

# List addresses of all incidents that occurred in Bronx or Queens.
#Number of incidents
query = "\
SELECT coursedb.incidents.address \
FROM (SELECT DISTINCT coursedb.boroughs.zipcode from coursedb.boroughs \
WHERE coursedb.boroughs.borough='Bronx' or 'Queens')x, coursedb.incidents \
WHERE coursedb.incidents.zipcode=x.zipcode;"

# Some addresses are none 
cur.execute(query)
for row in cur.fetchall() :
    if row[0] == None:
        pass
    else:
        print row[0]

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
