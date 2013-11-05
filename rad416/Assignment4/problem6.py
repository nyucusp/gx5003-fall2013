"""
A script to find all zipcodes in Manhattan where incidents have occurred
with their population. The output is sorted by zipcode and sent to STDOUT.
"""

import MySQLdb
# import warnings
# warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  cur = db.cursor()

  query = "SELECT zp.zcta, zp.total_population FROM zipcode_population zp INNER JOIN boroughs b ON b.zipcode = zp.zcta INNER JOIN incidents i ON b.zipcode = i.zipcode WHERE b.borough = 'Manhattan' and i.incidents > 0 GROUP BY zp.zcta ORDER BY zp.zcta" 
  cur.execute(query)
  result = cur.fetchall()
  print "The zipcodes where incidents have occurred in Manhattan with their populations:"
  for row in result:
    print row[0], row[1]

db.close()