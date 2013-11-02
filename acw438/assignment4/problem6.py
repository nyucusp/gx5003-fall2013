#Alex Chohlas-Wood (acw438). Assignment 4, Problem 6.

import sys
import MySQLdb
from decimal import *

#Establish variables
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')
cur = db.cursor()

cur.execute("SELECT DISTINCT B.zip, P.population FROM zip_incidents AS I, zip_boroughs as B, zip_population_area as P WHERE I.zip = B.zip AND I.zip=P.zip AND B.borough = 'MANHATTAN' LIMIT 100;")

for incident in cur.fetchall():
    print incident[0]

db.close()
