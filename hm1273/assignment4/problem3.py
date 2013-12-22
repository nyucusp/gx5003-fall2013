# Generated after group tutoring session
# Problem 3: compute the ratio of incidents to population in given borough. 
# Results not coming out due to "None" validation on Fetchall, but i did not know how to solve this.

import sys
import MySQLdb
import csv

borough = sys.argv[1]

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="hm1273", # your username
                   passwd="SQLuser", # your password
                   db="hmcoursedb") # name of the data base

# The Cursor object to execute the sql commands
cur = db.cursor() 

incidentData = "select sum(count) from (select count(zipcode) as count from incidents where zipcode in (select zipcode from zipBoroughs where borough = '"+borough+"') group by zipcode) as counts;"

populationData = "select sum(population) from zipcodes where zipcode in (select zipcode from zipBoroughs where borough = '"+borough+"');"

cur.execute(incidentData)
Incidents_Count = cur.fetchall()[0][0]

cur.execute(populationData)
Borough_Pop = cur.fetchall()[0][0]
if Borough_Pop is None:
    print 'None'
    sys.exit(0)

ratio = round(Incidents_Count / Borough_Pop, 3)

print "The incidents-to-population ratio in "+borough+" is "+str(ratio)+" incidents per person"




