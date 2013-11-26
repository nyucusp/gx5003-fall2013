# Awais Malik
# Assignment 4
# Problem 1
# Collaborated with Ender Faruk Morgul

import MySQLdb
import csv
import warnings
   
# Connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="am5801", # your username
                       passwd="12345", # your password
                       db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()

# Deal with warnings regarding table already exists
warnings.filterwarnings("ignore", "Unknown table.*")

drop_query="DROP table IF EXISTS coursedb.boroughs"
cur.execute(drop_query)

drop_query2="DROP table IF EXISTS coursedb.zipcodes"
cur.execute(drop_query2)

drop_query3="DROP table IF EXISTS coursedb.incidents"
cur.execute(drop_query3)

# Creating the boroughs table
boroughs_data = csv.reader(file('boroughs.csv'))
createCommand1 = "create table boroughs (id int UNIQUE AUTO_INCREMENT, zip int not null, bname varchar(100), primary key(id))"
cur.execute(createCommand1)
# Insert the csv_reader file using as strings in sql
for row in boroughs_data:
	cur.execute('insert into boroughs (''zip'',''bname'') values (%s,%s)',row)

# Creating the zipcodes table
zipcodes_data = csv.reader(file('zipCodes.csv'))
createCommand2 = "create table zipcodes (id int UNIQUE AUTO_INCREMENT, name varchar(100) not null, zip varchar(100) not null, \
zt36d00 varchar(100) not null, perimeter varchar(100) not null, lsadtr varchar(100) not null,zt36d00i varchar(100) not null, \
lsad varchar(100) not null, area varchar(100), latitude varchar(100), longitude varchar(100), population varchar(100), primary key(id))"
cur.execute(createCommand2)
for row in zipcodes_data:
	cur.execute('insert into zipcodes (''name'',''zip'',''zt36d00'',''perimeter'',''lsadtr'',''zt36d00i'',''lsad'',''area'',''latitude'',''longitude'',''population'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)

# Creating the incidents table
incidents_data = csv.reader(file('Incidents_grouped_by_Address_and_Zip.csv'))
createCommand3 = "create table incidents (id int UNIQUE AUTO_INCREMENT, address varchar(100) , zip varchar(100), \
uniquekey varchar(100) not null, primary key(id))"
cur.execute(createCommand3)
for row in incidents_data:
	cur.execute('insert into incidents (''address'',''zip'',''uniquekey'') values (%s,%s,%s)',row)

# Remove the first tuple with the titles
delhead1='DELETE FROM coursedb.zipcodes WHERE coursedb.zipcodes.id=1'
delhead2='DELETE FROM coursedb.incidents WHERE coursedb.incidents.id=1'
cur.execute(delhead1)
cur.execute(delhead2)

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# Close Connection
db.close()