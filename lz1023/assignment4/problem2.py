import MySQLdb
import sys
zip_input = sys.argv[1]
#connect to database
db=MySQLdb.connect(host="localhost",
	               user="lz1023",
	               passwd="19600313",
	               db="coursedb")
cur=db.cursor()

#query population density
query= "select (population/area) from zipcodes where zip= "+"'"+zip_input+"'"+";"
cur.execute(query)
density=cur.fetchall()
for row in density:
	print row[0]

db.close()	