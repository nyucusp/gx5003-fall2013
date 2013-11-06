import MySQLdb
import sys 
input = str(sys.argv[1])

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  
cur = db.cursor()   

 ### borough input into zipcode 

query = "select zipcode from borough where borough_name = "+ "'" + input + "'"
zipcodes_by_borough = [] 
cur.execute(query)
for row in cur.fetchall() :
    zipcodes_by_borough.append(row[0])


incidents_all = [] 
population_all = []
for i in zipcodes_by_borough: 
	query2 = "select incident from incidents where zipcode = " + "'" + i + "'" 
	cur.execute(query2)
	for row in cur.fetchall() :
		incidents_all.append(float(row[0]))
#		print incidents_all
#		print sum(incidents_all)
	query3 = "select population_of_zip from zipcode where zipcode = " + "'" + i + "'" 
	cur.execute(query3)
	for row in cur.fetchall() :
		population_all.append(float(row[0]))
#		print population_all
#		print sum(population_all)

print sum(incidents_all)/sum(population_all)


db.close() 
