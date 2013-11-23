#Katherine Elliott
#ke638
#Assignment 4
#Problem 3

import MySQLdb
import sys
   
 #connect to database
db = MySQLdb.connect(host="127.0.0.1",
                    user="ke638", # your username
                    passwd="10plus22", # your password
                    db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
cur = db.cursor() 

input = sys.argv
input.population_perZip(0)
input_borough = input[0].split()[0]

#total population of zipcode
query = "SELECT sum(key) FROM Boroughs_table JOIN Zipcodes_table WHERE borough = " + "'" + input_borough + "'" + "AND Boroughs_table.zipcode = Zipcodes_table.zip;"
cur.execute(query)

population = 0

for row in cur.fetchall():
    population += row[0]

#total population in zip code
query2 = "SELECT sum(key) FROM Incidents_Table join Boroughs_table where borough = " + "'" + input_borough + "'" + "and Boroughs_table.zipcode = Incidents_table.incident_zip;"
cur.execute(query2)

incidents = 0

for row in cur.fetchall():
    incidents += row[0]

print incidents/population

db.close()