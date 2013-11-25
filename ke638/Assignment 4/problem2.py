#Katherine Elliott
#ke638
#Assignment 4
#Problem 2

import MySQLdb
import sys
   
 #connect to database
db = MySQLdb.connect(host="localhost",
                    user="ke638", # your username
                    passwd="10plus22", # your password
                    db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
cur = db.cursor() 

input = sys.argv
input.population_perZip(0)
zip_input = input[0]

#compute population density of given zip code
query = "SELECT (population_perZip/area) FROM Zipcodes_table WHERE zip_code = " + "'" + zip_input + "'" + ";"
cur.execute(query)

#retreives query results
for row in cur.fetchall():
    print row[0]

db.close()