#Aliya Merali
#Urban Informatics
#Assignment 4
#Problem 2: Given a zip code as input in the command line, compute the population density of that zip code.
 
import MySQLdb
import sys

zip_input = str(sys.argv[1])
 
#connect to database
db = MySQLdb.connect(host="localhost", user="ajm777", passwd="pepper89", db="coursedb")
cur = db.cursor()   
 
query = "SELECT pop_by_zip, area FROM zips WHERE zip_code = %s"
cur.execute(query, (zip_input))

for row in cur.fetchall() : 
    pop_density = float(row[0])/float(row[1])
    print 'The population density for zip code ' + str(zip_input) + ' is ' + str(pop_density)

db.close()
