import MySQLdb
# import warnings
# warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rad416", # your username
                       passwd="mysql", # your password
                       db="coursedb") # name of the data base

with db:

  # The Cursor object will let you execute the sql commands
  cur = db.cursor()

  query = "SELECT zp.zcta, zp.total_population FROM zipcode_population zp INNER JOIN boroughs b ON b.zipcode = zp.zcta INNER JOIN incidents i ON b.zipcode = i.zipcode WHERE b.borough = 'Manhattan' and i.incidents > 0" 
  cur.execute(query)

  for row in cur:
    print row

db.close()