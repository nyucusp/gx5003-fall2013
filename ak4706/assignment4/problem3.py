import csv
import sys
import MySQLdb

#connect to database
db = MySQLdb.connect(host='localhost',
    user='ak4706',
    passwd='Atara7890',
    db = 'coursedb')
cursor = db.cursor()

#the inputed borough
borinput = sys.argv[1]

#first query to just get the zips from the inputed borough and enter them to borzip
borzip=[]
query1 = "SELECT DISTINCT Zip FROM Borough WHERE Borough = %s"
cursor.execute(query1, borinput)

for row in cursor.fetchall():
	borzip.append(int(row[0]))
#print borzip

# now get the population by zipcode for the zipcodes in the given borough
totalp = 0
tcount = 0
for line in borzip:
	query2 = "SELECT DISTINCT Zipcode.pop FROM zipcode, Borough WHERE Zipcode.Zip = %s"
	cursor.execute(query2, line)
	#now add up the population in that borough
	for row in cursor.fetchall():
		totalp = totalp + int(row[0])
		#print "pop", totalp

#same thing for the incidents per zipode - count them for zipcodes in that borough
for line in borzip:
	query3 = "SELECT DISTINCT Inczip, Incnum FROM Incidents WHERE Inczip = %s"
	cursor.execute(query3, line)
	for row in cursor.fetchall():
		tcount += row[1]
		#print "count", tcount
#calculate the ratio
ratio = float(tcount)/float(totalp)

print "The ratio of incidents to population in " + borinput + " is " + ratio 

db.close()