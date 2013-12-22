import sys
#This program creates 3 tables to store the three data sets (boroughs, zipCodes, & incidents)
#It also reads the data from the csv files and into the tables created

import MySQLdb
import csv


#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="hm1273", # your username
                   passwd="SQLuser", # your password
                   db="hmcoursedb") # name of the data base

# The Cursor object will let us execute the sql commands
cur = db.cursor()  

# We drop any existing tables to avoid issues when the program is run more than once
# When the table does not exist, we just get a warning, which is not a hard error, i.e. not a show stopper
cur.execute("DROP TABLE IF EXISTS boroughs")
cur.execute("DROP TABLE IF EXISTS zipcodes")
cur.execute("DROP TABLE IF EXISTS incidents")

#Create or Re-create the three tables with each dataset's respective attributes as fields
#Each table also has an integer id field that auto-increments for each new records created

createCommand = "create table boroughs (id int not null auto_increment, zipcode int not null, borough varchar(10), primary key(id))"
cur.execute(createCommand)              

# We could reuse the same "createCommand" like the tutorial, but we leave it this way for clarity
createCommand2 = "create table zipcodes (id int not null auto_increment, zipcode varchar(5), area double, population int, primary key(id));"
cur.execute(createCommand2)              
createCommand3 = "create table incidents (id int not null auto_increment, address varchar(100),zipcode int not null, primary key(id));"
cur.execute(createCommand3)              


#Read data from each file and insert into respective table, with a lot of similar tricks/commands. Comments skipped on repeated usage of same command

#Boroughs
boroughsCSVdata = open('boroughs.csv','rb') #returns list of lists, i.e. each element is a list that needs to be taken apart
#No header to drop
for Borough_Zip in boroughsCSVdata: 
    zip_element = Borough_Zip.split(',')[0]
    Borough_element = Borough_Zip.split(',')[1]
    insertCommand1 = "insert into boroughs (zipcode, borough) values ("+zip_element+", '"+Borough_element[0:-1]+"');"
    cur.execute(insertCommand1)


#ZipCodes
zipcodesCSVdata = open('zipCodes.csv','rb')
next(zipcodesCSVdata) #Dropping the header
for zipcode in zipcodesCSVdata:
    zip_element = zipcode.split(',')[0]
    zipArea_element = float (zipcode.split(',')[7]) 
    
    if(zipcode.split(',')[10][:-1] != ''):
        Population_Count = int(zipcode.split(',')[10])
    insertCommand = "insert into zipcodes (zipcode, area, population) values ('"+zip_element+"', "+str(zipArea_element)+", "+str(Population_Count)+");"
    cur.execute(insertCommand)

#Incidents
incidents_csv = open('Incidents_grouped_by_Address_and_Zip.csv','rb')
next(incidents_csv)
for incident in incidents_csv:
    zip_element = incident.split(',')[1]
    Address_element = incident.split(',')[0].replace("'",'')
    if(zip_element != '' and zip_element.isdigit()):
        insertCommand = "insert into incidents (address, zipcode) values('"+Address_element+"', "+str(zip_element)[:5]+");"
        cur.execute(insertCommand)


db.commit()
db.close()
