#Alex Chohlas-Wood (acw438). Assignment 4, Problem 3.

#NOTE: boroughs.csv is missing some fairly significant zipcodes, such as 10065.

import sys
import MySQLdb
from decimal import *

#Establish variables
boroughQuery = sys.argv[1]
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')
cur = db.cursor()


#Calcuate Ratio

#get total number of incidents by zip
query = "SELECT SUM(I.incidents) " + \
        "FROM zip_incidents AS I, zip_boroughs AS B " + \
        "WHERE B.borough = '" + boroughQuery + "' AND B.zip = I.zip;"
cur.execute(query)
boroughIncidentCount = Decimal(cur.fetchall()[0][0])

#get total population of borough by zip
query = "SELECT SUM(P.population) " + \
        "FROM zip_population_area AS P, zip_boroughs AS B " + \
        "WHERE B.borough = '" + boroughQuery + "' AND B.zip = P.zip;"
cur.execute(query)
boroughPopulation = Decimal(cur.fetchall()[0][0])

#Print ratio
print boroughIncidentCount/boroughPopulation

#Query to see a selection of Manhattan zips not included in boroughs.csv:
#SELECT * FROM zip_incidents AS I WHERE I.zip LIKE "100__" AND NOT EXISTS(SELECT * FROM zip_boroughs AS B WHERE I.zip=B.zip) LIMIT 100;

db.close()
