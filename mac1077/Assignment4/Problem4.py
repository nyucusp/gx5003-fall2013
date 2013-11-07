import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="mac1077",passwd="miquel",db="coursedb")
cur=db.cursor()

querry="SELECT address FROM boroughs b INNER JOIN incidents i ON b.zip = i.zip WHERE borough_name='Manhattan' AND address > '' group by address;"
cur.execute(querry)

for row in cur.fetchall():
        print row[0]
db.close