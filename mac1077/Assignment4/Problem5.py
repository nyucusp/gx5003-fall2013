import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="mac1077",passwd="miquel",db="coursedb")
cur=db.cursor()

querry="SELECT address FROM boroughs b INNER JOIN incidents i ON b.zip=i.zip WHERE b.borough_name = 'Bronx' or'Queens' AND address > '' group by address;"
cur.execute(query)

for row in cur.fetchall():
        print row[0]

db.close()