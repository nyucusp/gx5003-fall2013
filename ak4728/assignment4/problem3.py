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

boroughname = sys.argv[1]
##boroughname = 'Manhattan'

#Given a borough name, your task is to compute the ratio between the number of incidents and the population in that borough.

#Number of incidents
query = "\
SELECT SUM(coursedb.incidents.uniquekey) \
FROM (SELECT DISTINCT coursedb.boroughs.zipcode from coursedb.boroughs \
WHERE coursedb.boroughs.borough='"+boroughname+"')x, coursedb.incidents \
WHERE coursedb.incidents.zipcode=x.zipcode;"

cur.execute(query)
for row in cur.fetchall() :
    if row[0] == None:
        print "Zipcode is not in the list of zipcodes, try again.1"
    else:
        numOfIncidents=row[0]


#Population
query2 = "SELECT sum(y.popper)  FROM (SELECT DISTINCT coursedb.boroughs.zipcode from coursedb.boroughs \
WHERE coursedb.boroughs.borough='"+boroughname+"') x, coursedb.zipcode y WHERE y.zipcode=x.zipcode;"
cur.execute(query2)


# process the result. Here I am just printing out the rows


for row in cur.fetchall() :
    if row[0] == None:
        print "Zipcode is not in the list of zipcodes, try again.2"
    else:
        print 'The ratio between the number of incidents and the population is '\
              + str(float(numOfIncidents)/float(row[0])) + ' in ' + str(boroughname)


# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
