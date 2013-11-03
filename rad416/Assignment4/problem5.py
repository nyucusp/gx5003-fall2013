import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rad416", # your username
                       passwd="mysql", # your password
                       db="coursedb") # name of the data base

with db:

  cur = db.cursor()

  query = "SELECT address FROM incidents i INNER JOIN boroughs b ON b.zipcode = i.zipcode WHERE b.borough = 'Queens' or b.borough = 'Bronx' AND address > '' GROUP BY address ORDER BY address"
  cur.execute(query)
  result = cur.fetchall()
  print "The address for incidents occurring in Queens or the Bronx are:"
  for row in result:
    print row[0]

db.close()