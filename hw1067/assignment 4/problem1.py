"""
Assignment 4
problem 1
Haozhe Wang
"""
import csv
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="hw1067",
                     passwd="81828384yomama",
                     db="coursedb")

cur = db.cursor()
#setup the cursor, connect to database
cur.execute("DROP TABLE IF EXISTS boroughs")
cur.execute("DROP TABLE IF EXISTS zips")
cur.execute("DROP TABLE IF EXISTS incident")
#import all three files
zipcode_file = open('zipCodes.csv', 'r')
borough_file = open('boroughs.csv', 'r')
incident_file = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')


# crete tables
table_zip = "create table zips (zip_code int not null, area float not null, pop_by_zip int )"
table_borough = "create table boroughs (zip_code int not null, name varchar(50) not null)"
table_incident = "create table incident (address varchar(500), zip_code int not null, num_inc int)"
 
cur.execute(table_zip)
cur.execute(table_borough)
cur.execute(table_incident)

n = 0
#zip_split = []
zipcodecon = csv.reader(zipcode_file,delimiter= ',')
for line in zipcodecon:
    if n == 0:
        n+=1
        continue
    else:
        zip_name = line[0]
        area = line[7]
        pop = line[10]
        #print pop
        if pop!= '' :
        #print line_split[10]
            insertCommand = "insert into zips values(" + str(zip_name) + "," + str(area) + "," + str(pop) + ");"
            #print insertCommand
            cur.execute(insertCommand)

for line in borough_file:
    line_split = line.split(',')
    zipcode = line_split[0]
    name = line_split[1]
    insertCommand = "insert into boroughs values("+ zipcode + "," + "'" + name + "'" + ");"
    cur.execute(insertCommand)


incidents = csv.reader(incident_file,delimiter= ',')

for x in incidents:
    if n == 0:
        n += 1
        continue
    else:
        address = x[0]
        zipcode = x[1]
        count = x[2]
        if (zipcode.isdigit()):
            address = address.replace("'","")
            insertCommand = "insert into incident values("+"'"+str(address)+"'"+","+"'"+str(zipcode)+"'"+","+str(count)+");"
            cur.execute(insertCommand)
db.commit()
db.close()
