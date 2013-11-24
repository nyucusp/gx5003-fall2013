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

# List the set of zip codes in Manhattan along with their population where incidents have occurred.
#Number of incidents
query = "\
SELECT h.zipcode, h.popper FROM (SELECT DISTINCT i.zipcode \
FROM (select distinct coursedb.boroughs.zipcode \
FROM coursedb.boroughs where coursedb.boroughs.borough='Manhattan') z, \
coursedb.incidents i WHERE z.zipcode = i.zipcode) k, \
coursedb.zipcode h WHERE k.zipcode=h.zipcode and h.popper is not null;"

# Some addresses are none 
cur.execute(query)
print 'zipcodes' + ' ' + 'population'
for row in cur.fetchall() :
    if row[0] == None:
        pass
    else:
        print row[0] + '\t' + row[1]

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
