#'to do: createCommand for incidents, and make sure everything is correct'



#Nathan Seltzer
#Assignment 4
#Problem 1

import MySQLdb

import csv

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="seltzn01", # your username
                      passwd="inform", # your password
                      db="coursedb") # name of the data base

cur = db.cursor()  



"""
BOROUGHS
"""
# #drop table if already exists
cur.execute("DROP TABLE IF EXISTS boroughs")
# # create a table with three attributes
createBoroughs = ("create table boroughs (zipcode varchar(5), borough varchar(255), primary key(zipcode))")
cur.execute(createBoroughs)

boroughsCSV = open('boroughs.csv', 'r')
blines = boroughsCSV.readlines()


boroughsCSV = csv.reader(file('boroughs.csv'))
myData = {}
for row in boroughsCSV:
	if not row[0] in myData: # getting rid of repated value 10451
		Bcommand = "insert into boroughs values(" + row[0] + ", '" + row[1] + "')"
		cur.execute(Bcommand)
		myData[row[0]] = row[1]
	else:
		print 'problem ' + row[0]




"""
INCIDENTS

"""

cur.execute("DROP TABLE IF EXISTS incidents")
#zipcode and unique key as strings because they are not values, but represent items
createIncidents = ("create table incidents(incident_address varchar(255), zipcode varchar(5), unique_key varchar(255), primary key(incident_address))")
cur.execute(createIncidents)
# Iid = ("ALTER TABLE incidents ADD id varchar(200), drop primary key, add primary key(id)")
# cur.execute(Iid)


incidentsCSV = open('boroughs.csv', 'r')
ilines = incidentsCSV.readlines()

incidentsCSV = csv.reader(file('Incidents_grouped_by_Address_and_Zip.csv'))
# Skip first line
next(incidentsCSV)

for row in incidentsCSV:	

	Icommand = "insert into incidents values('" + row[0] + "', '" + row[1] + "', '" + row[2] + "'')"
	cur.execute(Icommand)



"""
zipcodes
"""

# cur.execute("DROP TABLE IF EXISTS zipcodes")
# createZipcodes = ("create table zipcodes (zipcode int, zipcode_tabulation_area int,zt36_d00 int, perimeter float, lsad_trans varchar(255), zt36_d00_i int, lsad varchar(255), area float, latitude float, longitude float, TotalPopulation int, primary key (zipcode))")
# cur.execute(createZipcodes)

# zipcodesCSV = csv.reader(file('zipcodes.csv'))
# Zcommand = "insert into incidents values('" + row[0] + "', '" + row[1] + "', '" + row[2] + "'', '" + row[3] + "'', '" + row[4] + "'', '" + row[5] + "'', '" + row[6] + "'', '" + row[7] + "'', '" + row[8] + "'', '" + row[9] + "'', '" + row[10] + "'')"
# for row in zipcodesCSV:
# 	cur.execute(Zcommand)



db.commit()	
# close connection
db.close()