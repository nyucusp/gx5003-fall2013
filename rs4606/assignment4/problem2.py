import MySQLdb
import sys

# Here we save the user's input zip code as given_zip
input = sys.argv
input.pop(0)
given_zip = input[0]

# Here we connect to the database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rs4606", # your username
                       passwd="a1s2d3f4", # your password
                       db="coursedb") # name of the data base  

cur = db.cursor()   

# In this query we compute the population density for the desired zip code.
query = "select (population/area) from zipcodes where zip = " + "'" + given_zip + "'" + ";"

cur.execute(query)

# Here we print the population density
for row in cur.fetchall():
 	print row[0]


db.close()
