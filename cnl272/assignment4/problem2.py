#Problem 2: Given a zip code as input in the command line, compute the population density of that zip code.

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="cnl272",passwd="p00p00",db="coursedb")
cur = db.cursor()

zip_code=sys.argv[1]

query = "SELECT (population/area) from zipcodes where zip = "+"'"+zip_code+"'"+";"
cur.execute(query)

for row in cur.fetchall():
	print row[0]

db.close()