"""
A script that takes in a borough name as an argument and returns the number of incidents by
population.  The borough name does not need to be capitalized and a test is made to append 
"Island" to the end of Staten to make it standard on the output.
"""

import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  cur = db.cursor()

  query = "SELECT bp.borough, bi.borough_incidents/bp.borough_pop as incident_pop_ratio FROM( SELECT b.borough borough, SUM(total_population) borough_pop FROM zipcode_population zp INNER JOIN boroughs b ON b.zipcode = zp.zcta WHERE b.borough = '" + sys.argv[1] + "' GROUP BY b.borough ) as bp INNER JOIN ( SELECT b.borough borough, SUM(incidents) borough_incidents FROM incidents i INNER JOIN boroughs b ON b.zipcode = i.zipcode WHERE b.borough = '" + sys.argv[1] + "' GROUP BY b.borough ) as bi ON bi.borough = bp.borough"
  cur.execute(query)

  result = cur.fetchall() #fetch all results from cur and bind to variable
  if len(result) > 0:
    for row in result: #iterate through results
      if row[0] == "Staten": #test for Staten Island
        print "The ratio of incidents to population in " + row[0] + " Island is " + str(row[1])
      else: #borough is not Staten Island
        print "The ratio of incidents to population in " + row[0] + " is " + str(row[1])
  else:
    print sys.argv[1] + " isn't a NYC borough"
db.close()