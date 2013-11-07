    ##########################
    #  Assignment4 Problem5  #
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

query = "SELECT address FROM incident AS i INNER JOIN boroughs AS b ON i.zip_code = b.zip_code WHERE b.name = 'Bronx' OR 'Queens';"
cur.execute(query)

for row in cur.fetchall():
    print row

 # close connection
db.close()
