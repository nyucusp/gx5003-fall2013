"""
A script to find the addresses of all incidents occurring in either Bronx
or Queens.  Empty addresses are omitted and the output is sorted.  The script
output is sent to STDOUT.
"""

import MySQLdb

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  cur = db.cursor()

  query = "SELECT address FROM incidents i INNER JOIN boroughs b ON b.zipcode = i.zipcode WHERE b.borough = 'Queens' or b.borough = 'Bronx' AND address > '' GROUP BY address ORDER BY address"
  cur.execute(query)
  result = cur.fetchall()
  print "The address for incidents occurring in Queens or the Bronx are:"
  for row in result:
    print row[0]

db.close()