#Aliya Merali
#Urban Informatics
#Assignment 4
#Problem 6: List the set of zip codes in Manhattan along with their population where incidents have occurred.

#I read this assignment to mean that you'd like the MN zip codes and the population in zip codes in which incidents were reported 
 
import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", user="ajm777", passwd="pepper89", db="coursedb")
cur = db.cursor()

query = "SELECT zip_code, pop_by_zip FROM zips WHERE zip_code IN (SELECT zip_code FROM bor WHERE name = 'Manhattan' AND zip_code IN (SELECT zip_code FROM inc))"
cur.execute(query)

for row in cur.fetchall():
    print str(row[0]), str(row[1])

db.close()
