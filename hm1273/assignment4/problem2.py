# Generated after group tutoring session
# Problem 2: compute the population density of a zip code given as input in the command line, generated after group tutoring session. 

#note about alpha zip codes: all have blanks. We do not account here for that
#lots of issues in file, such as zip code having letters, and also note lots of unnecessary columns

import sys
import MySQLdb

zip_code = sys.argv[1]

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="hm1273", # your username
                   passwd="SQLuser", # your password
                   db="hmcoursedb") # name of the data base

# The Cursor object to execute the sql commands
cur = db.cursor() 

find_pop_density_per_zip = "select population/area from zipcodes where zipcode ='"+zip_code+"';"
cur.execute(find_pop_density_per_zip)

print str(cur.fetchall()[0])[1:-2]

