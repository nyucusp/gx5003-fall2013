#Alex Chohlas-Wood (acw438). Assignment 4, Problem 2.

import sys
import MySQLdb
from decimal import *

#Establish variables
zipQuery = sys.argv[1]
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')
cur = db.cursor()

#Run Query
query = 'SELECT population, area FROM zip_population_area WHERE zip="' + zipQuery + '";'
try:
    cur.execute(query)
    resultTuple = cur.fetchall()[0]
    population, area = resultTuple[0], resultTuple[1]
    #print population, area

    #Calculate output, round error
    area = (Decimal(population)/Decimal(area)).quantize(Decimal('.0001'), rounding=ROUND_UP)
    print area
except IndexError as errorM:
    print "The queried zipcode probably doesn't exist in the database. (" + str(errorM) + ")"
finally:
    db.close()
