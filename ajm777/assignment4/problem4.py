#Aliya Merali
#Urban Informatics
#Assignment 4
#Problem 4: List addresses of all incidents that occurred in Manhattan.
 
import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", user="ajm777", passwd="pepper89", db="coursedb")
cur = db.cursor()

query = "SELECT address FROM inc WHERE zip_code IN (SELECT zip_code FROM bor WHERE name = 'Manhattan')"
cur.execute(query)

for row in cur.fetchall():
    print row

db.close()
