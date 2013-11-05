import MySQLdb
import sys
#connect to database
db=MySQLdb.connect(host="localhost",
	               user="lz1023",
	               passwd="19600313",
	               db="coursedb")
cur=db.cursor()

query="select address from incidents i, borough b where name='Manhattan' and b.zip=i.zip;"
cur.execute(query)
address=cur.fetchall()
for row in address:
	print row[0]

db.close()	