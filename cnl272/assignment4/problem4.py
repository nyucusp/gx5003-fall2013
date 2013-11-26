#Problem 4: List addresses of all incidents that occurred in Manhattan.

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="cnl272",passwd="p00p00",db="coursedb")
cur=db.cursor()

querry="SELECT address FROM boroughs b INNER JOIN incidents i ON b.zip = i.zip WHERE borough_name='Manhattan' AND address > '' group by address;"
cur.execute(querry)

for row in cur.fetchall():
	print row[0]

db.close