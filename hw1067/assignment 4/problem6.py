    ##########################
    #  Assignment4 Problem6  #
    #  Haozhe Wang           #
    ##########################

import MySQLdb
#import sys

#boroughinput = sys.argv[1]

db = MySQLdb.connect(host = "localhost",
	user = "hw1067",
	passwd = "81828384yomama",
	db = "coursedb")
cur = db.cursor()

query = "SELECT intermediate.zip_code, pop_by_zip FROM (SELECT distinct incident.zip_code FROM boroughs INNER JOIN incident WHERE name = 'Manhattan' AND boroughs.zip_code = incident.zip_code) AS intermediate INNER JOIN zips WHERE intermediate.zip_code = zips.zip_code;"

cur.execute(query)

for row in cur.fetchall():
	print row[0],row[1]

# close connection
db.close()
