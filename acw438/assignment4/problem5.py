#Alex Chohlas-Wood (acw438). Assignment 4, Problem 5.

import sys
import MySQLdb
from decimal import *

#Establish variables
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')
cur = db.cursor()

cur.execute("SELECT I.address FROM zip_incidents AS I, zip_boroughs AS B WHERE I.zip = B.zip AND (B.borough = 'QUEENS' OR B.borough = 'BRONX')")

for incident in cur.fetchall():
    print incident[0]

db.close()
