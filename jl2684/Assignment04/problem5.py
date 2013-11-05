import MySQLdb
import sys 

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  
cur = db.cursor()   

query = "select zipcode from borough where borough_name = 'Bronx' or borough_name = 'Queens'" 
zipcodes_of_bronx_or_queens = [] 
cur.execute(query)
for row in cur.fetchall() :
    zipcodes_of_bronx_or_queens.append(row[0])

for i in zipcodes_of_bronx_or_queens: 
	query2 = "select address from incidents where incident > '0' AND zipcode = " + "'" + i + "'" 
	cur.execute(query2)
	for row in cur.fetchall() :
		if row[0] != '':
			print row[0]

db.close()  

