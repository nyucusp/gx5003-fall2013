import MySQLdb
import pandas as pd
import csv

#ZipCode database
db = MySQLdb.connect(host = 'localhost', user = 'ks2890', passwd = '12345', db ='coursedb')
cur = db.cursor()
#incidents database
droptable = 'drop table incidents'
cur.execute(droptable)
createCommand_incidents = 'create table incidents (address varchar(255), zipcode varchar(255), num_inc int, primary key(zipcode))'
cur.execute(createCommand_incidents)
print "incidents tables were created"

droptable = 'drop table zipCodes'
cur.execute(droptable)
createCommand_zip = 'create table zipCodes (zipcode varchar(255), area FLOAT, pop FLOAT, primary key(zipcode))'
cur.execute(createCommand_zip)

print "zipcode table created"

#Borough database
droptable = 'drop table boroughs'
cur.execute(droptable)
createCommand_boroughs = 'create table boroughs (zipcode varchar(255), borough varchar(255), primary key(zipcode))'
cur.execute(createCommand_boroughs)

print "boroughs table created"



#Read zipcode csv
with open('zipCodes.csv', 'r') as zipcodesfile:
	zipcodes = csv.reader(zipcodesfile)
	next(zipcodes)  # skip header row
	previous = []

	for line in zipcodes:
		zipcode = line[0]
		area = line[7]
		pop = line[10]
		if len(pop) > 0 and len(area) > 0 and zipcode not in previous:
		# create command to insert tis into the table
			insertCommand = "insert into zipCodes values (" + zipcode  + ", " + area + ", " + pop  +");"
			previous.append(zipcode)
			cur.execute(insertCommand)
db.commit()

#Read boroughs csv
with open('boroughs.csv', 'r') as boroughsfile:
	boroughs = csv.reader(boroughsfile)	
	previous = []

	for line in boroughs:
		zipcode = line[0]
		borough = line[1]
		if len(zipcode) > 0 and zipcode not in previous:
		# create command to insert tis into the table
			insertCommand = "insert into boroughs values ( %s, %s);"
			previous.append(zipcode)
			cur.execute(insertCommand,(zipcode, borough,))
db.commit()

#Read incident csv
with open('incidents.csv', 'r') as incidentsfile:
	incidents = csv.reader(incidentsfile)
	next(incidents)  # skip header row
	previous = []

	for line in incidents:
		address = line[0]
		zipcode = line[1]
		num_inc = line[2]
		if len(zipcode)>0 and zipcode not in previous:
		# create command to insert tis into the table
			insertCommand = "INSERT into incidents VALUES ( %s, %s, %s);"
			previous.append(zipcode)
			cur.execute(insertCommand,(address, zipcode, num_inc,))
db.commit()
db.close()