import csv
import sys
import MySQLdb

#connect to the database
db = MySQLdb.connect(host='localhost',
    				user='ak4706',
    				passwd='Atara7890',
    				db = 'coursedb')

cursor = db.cursor()

#query to get the addresses from incidents whose zips are in Manhattan 
query = "SELECT Incadd FROM Incidents WHERE Incidents.Inczip IN(SELECT Borough.Zip FROM Borough WHERE Borough = 'Manhattan')"
cursor.execute(query)

print "The following are addresses in Manhattan where incidents have occured:"
for row in cursor.fetchall():
	print row

db.close()