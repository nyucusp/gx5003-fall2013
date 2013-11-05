import MySQLdb
import sys 

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  

cur = db.cursor()   

query = "select zipcode from incidents where incident > '0' " 

cur.execute(query)
for row in cur.fetchall():
	query = "select zipcode from borough where borough_name = 'Manhattan' and zipcode =" + "'" + row[0] + "'"  
	cur.execute(query)
	for i in cur.fetchall():
		query = "select zipcode, population_of_zip from zipcode where zipcode = " + "'" + i[0] + "'"
		cur.execute(query)
		for z in cur.fetchall():
			print 'Zipcode:' + z[0] + ", Population:" + z[1] 




db.close() 