#Katherine Elliott
#ke638
#Assignment 4
#Problem 6

import MySQLdb
import sys
   
 #connect to database
db = MySQLdb.connect(host="127.0.0.1",
                    user="ke638", # your username
                    passwd="10plus22", # your password
                    db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
cur = db.cursor() 

query = "SELECT DISTINCT name, population_perZip FROM Zipcodes_table JOIN Boroughs_table WHERE borough = 'Manhattan' AND Boroughs_table.zipcode = Zipcodes_table.name;"
cur.execute(query)

for row in cur.fetchall():
    print row[0], row[1]

db.close()
