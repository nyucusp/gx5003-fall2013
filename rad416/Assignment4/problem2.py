"""
A script that takes in a zipcode from the command line and returns the population density.
The unit of area is likely decimal degrees, but is unspecified in the file. The number
is returned as provided without any attempt to find the units of measure.
"""

import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:
  cur = db.cursor()

  query = "SELECT total_population/area as density FROM zipcode_population WHERE zcta = '" + sys.argv[1] + "'" 
  cur.execute(query)

  result = cur.fetchall()
  if len(result) > 0:
    for row in result:
      print "The population density in zipcode " + sys.argv[1] + " is " + str(row[0])
  else:
    print "Zipcde " + sys.argv[1] + " is not in New York State"

db.close()