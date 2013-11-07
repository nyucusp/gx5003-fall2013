import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="mac1077",passwd="miquel",db="coursedb")
cur=db.cursor()

query = "SELECT b.zip, z.population FROM boroughs b, zipcodes z WHERE b.zip = z.zip AND b.borough_name = 'Manhattan' AND b.zip in (SELECT i.zip from incidents i);" 
cur.execute(query)
for row in cur.fetchall():
        print row[0],row[1]
db.close()