import MySQLdb
import sys
#connect to database
db=MySQLdb.connect(host="localhost",
	               user="lz1023",
	               passwd="19600313",
	               db="coursedb")
cur=db.cursor()

query="select b.zip, z.population from borough b, zipcodes z where b.zip=z.zip and name='Manhattan' and b.zip in(select i.zip from incidents i);"
cur.execute(query)
zippop=cur.fetchall()
for row in zippop:
	print row[0], row[1]
db.close()	