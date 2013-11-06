import MySQLdb
import sys
bor_input = sys.argv[1]
#connect to database
db=MySQLdb.connect(host="localhost",
	               user="lz1023",
	               passwd="19600313",
	               db="coursedb")
cur=db.cursor()

query = "select sum(population) from borough, zipcodes where name = " + "'" +bor_input + "'" + "and borough.zip=zipcodes.zip; "
cur.execute(query)
total_pop=cur.fetchall()[0][0]

query = "select sum(incident_num) from borough, incidents where name = " + "'" +bor_input + "'" + "and borough.zip=incidents.zip; "
cur.execute(query)
total_inc=cur.fetchall()[0][0]

ratio=total_inc/total_pop
print ratio

db.close()
