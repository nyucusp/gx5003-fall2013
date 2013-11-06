#Kara Leary
#Urban Informatics - Assignment 4
#Problem 1

import MySQLdb
import csv

db = MySQLdb.connect(host="localhost", user="kll392", passwd="Maywalsh1", db="coursedb")
cur = db.cursor()

#Create boroughs table:
createBoroughs = "create table boroughs (zip int not null, borough varchar(255), primary key(zip))"
cur.execute(createBoroughs)

#Create zip codes table:
createZipCodes = "create table zipcodes (zip int not null, area double, population int, primary key(zip))"
cur.execute(createZipCodes)

#Create incidents table:
createIncidents = "create table incidents (incidentID int not null, address varchar(255), zip int, primary key(incidentID))"
cur.execute(createIncidents)

#Insert values from boroughs.csv into boroughs table:
with open('boroughs.csv') as f:
    rows = csv.reader(f, delimiter=',')
    for row in rows:
        zip = row[0]
        borough = row[1].lower()
        #Check for duplicate values of zip codes in table:
        checkDuplicates = "(SELECT * FROM boroughs WHERE zip =" + zip + ");"
        if cur.execute(checkDuplicates) != 1:
            insertCommand = "insert into boroughs values(" + str(zip) + "," + "'" + borough + "');"
            cur.execute(insertCommand)

#Insert values from zipcodes.csv into zipcodes table:
with open('zipCodes.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        #Only add value to table if the zip code has a population entry associated with it:
        if (row[10] != ''):
            zip = row[0]
            area = row[7]
            population = row[10]
            #Check for duplicate zip codes- if duplicate exists, assume the first one is correct:
            checkDuplicates = "(SELECT * FROM zipcodes WHERE zip =" + zip + ");"
            if cur.execute(checkDuplicates) != 1:
                insertCommand = "insert into zipcodes values(" + str(zip) + "," + str(area) + "," + str(population) + ");"
                cur.execute(insertCommand)
         
#This function tests for the object type; it will be used to help determine if a zip code value is null in the incident table:
tests = [(int, int)]
def getType(value):
    for typ, test in tests:
        try:
            test(value)
            return typ
        except ValueError:
            continue
    return str

#Create primary key called "incidentID"
incidentID = 0   
with open('Incidents_grouped_by_Address_and_Zip.csv') as f:
    rows = csv.reader(f, delimiter=',')
    rows.next()
    for row in rows:
        incidentID += 1
        address = row[0]
        #Replace any apostrophes in address column so that they do not affect the SQL query:
        address = address.replace("'", "''")
        zip = row[1]
        #If a zip code entry is empty or a string (i.e. N/A), make the entry null in SQL:
        if getType(zip) != int:
            zip = 'NULL'
        insertCommand = "insert into incidents values(" + str(incidentID) + "," + "'" + address + "'" + "," + str(zip) + ");"
        cur.execute(insertCommand)


db.commit()
db.close()
