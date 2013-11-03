import sys
from _collections import defaultdict
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

  query = "SELECT total_population/area as density FROM zipcode_population WHERE zcta = '" + sys.argv[1] + "'" 
  cur.execute(query)

  for row in cur:
    print row
  # print query

db.close()