import sys
from _collections import defaultdict
import MySQLdb
# import warnings
# warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", user="rad416", passwd="mysql", db="coursedb")

with db:

  # The Cursor object will let you execute the sql commands
  cur = db.cursor()

  query = "SELECT total_population/area as density FROM zipcode_population WHERE zcta = '" + sys.argv[1] + "'" 
  cur.execute(query)

  result = cur.fetchall()
  if len(result) > 0:
    for row in result:
      print "The population density in " + sys.argv[1] + " is " + str(row[0])
  else:
    print "Zipcde " + sys.argv[1] + " is not in New York City"

db.close()