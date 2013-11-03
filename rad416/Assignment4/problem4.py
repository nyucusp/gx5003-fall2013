"""
A script to find every address where an incident occured in Manhattan. Blank 
addresses have been removed and the addresses sorted. The file output goes to
STDOUT.
"""

import MySQLdb

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  cur = db.cursor()

  query = "SELECT address FROM incidents i INNER JOIN boroughs b ON b.zipcode = i.zipcode WHERE borough = 'Manhattan' AND address > '' GROUP BY address ORDER BY address"
  cur.execute(query)
  result = cur.fetchall()
  for row in result:
    print row[0]

db.close()