import csv
import sys
import MySQLdb

#connect to database
db = MySQLdb.connect(host='localhost',
    				user='ak4706',
    				passwd='Atara7890',
    				db = 'coursedb')

cursor = db.cursor()

#query to get the addresses from incidents whose zips are in Queens and Bronx
query = "SELECT Incadd FROM Incidents WHERE Incidents.Inczip IN(SELECT Borough.Zip FROM Borough WHERE Borough = 'Queens' or Borough = 'Bronx')"
cursor.execute(query)

print "The following are addresses in the Bronx or Queens where incidents have occured:"
for row in cursor.fetchall():
	print row

db.close()