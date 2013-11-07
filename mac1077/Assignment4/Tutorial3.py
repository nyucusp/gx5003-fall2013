import MySQLdb
 
 
db = MySQLdb.connect(host="localhost", user="mac1077", passwd="miquel", db="coursedb") 
cur = db.cursor()   

query = "select * from test where age < 25"
cur.execute(query)

for row in cur.fetchall() :
	print str(row[0]) + " " + row[1] + " " + str(row[2])

db.close()