import MySQLdb
import sys 

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  
 # The Cursor object will let you execute the sql commands
cur = db.cursor()   

### borough input into zipcode 

query = "select zipcode from borough where borough_name = 'Manhattan'" 
zipcodes_of_manhattan = [] 
cur.execute(query)
for row in cur.fetchall() :
    zipcodes_of_manhattan.append(row[0])

for i in zipcodes_of_manhattan: 
	query2 = "select address from incidents where incident > '0' AND zipcode = " + "'" + i + "'" 
	cur.execute(query2)
	for row in cur.fetchall() :
		if row[0] != '':
			print row[0] 


db.close() 
