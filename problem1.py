#Katherine Elliott
#ke638
#Assignment 4
#Problem 1

import MySQLdb
import csv
   
 #connect to database
db = MySQLdb.connect(host="localhost",
                    user="ke638", # your username
                    passwd="10plus22", # your password
                    db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()  

dropcommand = "DROP TABLE IF EXISTS boroughs_table"
cur.execute(dropcommand)

dropcommand = "DROP TABLE IF EXISTS zipcodes_table"
cur.execute(dropcommand)

dropcommand = "DROP TABLE IF EXISTS incidents_table"
cur.execute(dropcommand)

createCommand = "CREATE table Boroughs_table (zipcode int not null, borough varchar(10), primary key(zipcode))"
cur.execute(createCommand)

createCommand = "CREATE table ZipCodes_table (name int not null, zip int not null, area int not null, population_perZip int not null, primary key(name))"
cur.execute(createCommand)

createCommand = "CREATE table Incidents_table (incident_address varchar(255), incident_zip int not null, name int not null, population_perZip int not null, primary key(incident_address))"
cur.execute(createCommand)

open('boroughs.csv')
boroughs_csv = csv.reader(file('boroughs.csv', 'rb'))
for row in boroughs_csv:
    zipcode = row[0]
    borough = row[1]
    selectzips = "(SELECT * FROM Boroughs_table where zipcode =" + zipcode + ");"
    if cur.execute(selectzips) != 1:
        insertCommand = "INSERT into Boroughs_table values(" + str(zipcode) + "," + "'" + borough + "');"
        cur.execute(insertCommand)

open('zipcode.csv')
zipcodes_csv = csv.reader(file('zipcode.csv', 'rb'))
next(zipcodes_csv)
for row in zipcodes_csv:
    next(zipcodes_csv)
    if row[10] != ' ':#select only if associated with population
        name = row[0]        
        zip = row[1]
        area = row[7]
        population_perZip = row[10]
        selectpop = "(SELECT * FROM ZipCodes where zip =" + zip + ");" #eliminate duplicates
        if cur.execute(selectpop) != 1:
            insertCommand = "INSERT into Zipcodes_table values(" + str(name) + "," + "'" + str(zip) + "'"+"," + str(area) + "'" + "," + str(population_perZip) + ");"
            cur.execute(insertCommand)

open('incidents.csv')
incidents_csv = csv.reader(file('incidents.csv', 'rb'))
next(incidents_csv)
for row in zipcodes_csv:
    if row[1] != ' ':#select only if associated with incident zipcode
        incident_address = row[0]        
        incident_zip = row[1]
        name = row[2]
        population_perZip = row[10]
        insertCommand = "INSERT into Incidents_table values(" + incident_address + "," + "'" + str(incident_zip) + "'" + "," + str(name) + "'" + str(population_perZip) + ");"
        cur.execute(insertCommand)

db.commit()
db.close()


    
