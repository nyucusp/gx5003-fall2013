import MySQLdb
import csv

incidentsFile = open('Incidents_grouped_by_Address_and_Zip.csv','rb')
boroughsFile = open('boroughs.csv','rb')
zipcodesFile = open('zipCodes.csv','rb')


db = MySQLdb.connect(host="localhost", user="agb344", passwd="amir", db="assignment4")

cur = db.cursor()

createBoroughs = "create table zipBoroughs (id int not null auto_increment, zipcode int not null, borough varchar(10), primary key(id))"
createZipcodes = "create table zipcodes (id int not null auto_increment, zipcode varchar(5), area double, population int, primary key(id));"
#createIncidents = "create table incidents (id int not null auto_increment, address varchar(50), zipcode int not null, primary key(id));"
createIncidents = "create table incidents (id int not null auto_increment, address varchar(100),zipcode int not null, primary key(id));"

cur.execute(createZipcodes)
cur.execute(createBoroughs)
cur.execute(createIncidents)

for zipBorough in boroughsFile:
    thisZip = zipBorough.split(',')[0]
    thisBorough = zipBorough.split(',')[1]
    insertCommand = "insert into zipBoroughs (zipcode, borough) values ("+thisZip+", '"+thisBorough[0:-1]+"');"
    #boroughDict[thisBorough.lower()[:-1]].append(thisZip)
    #print insertCommand
    #print insertCommand
    cur.execute(insertCommand)

zipcodesFile.readline()
for zipcode in zipcodesFile:
    #print zipcode
    thisParse = zipcode.split(',')
    thisZipName = thisParse[0]
    thisZipArea = float(thisParse[7])
    if(thisParse[10][:-1] != ''):
        #print thisParse[10]
        thisZipPopulation = int(thisParse[10])
    #print thisZipName, thisZipArea, thisZipPopulation
    insertCommand = "insert into zipcodes (zipcode, area, population) values ('"+thisZipName+"', "+str(thisZipArea)+", "+str(thisZipPopulation)+");"
    #print insertCommand
    cur.execute(insertCommand)

incidentsFile.readline()

for incident in incidentsFile:
    thisParse = incident.split(',')
    thisZipName = thisParse[1]
    thisAddress = thisParse[0].replace("'",'')
    if(thisZipName != '' and thisZipName.isdigit()):
        insertCommand = "insert into incidents (address, zipcode) values('"+thisAddress+"', "+str(thisZipName)[:5]+");"
        cur.execute(insertCommand)
'''
for incident in incidentsFile:
    thisParse = incident.split(',')
    thisZipName = thisParse[1]
    if(thisZipName != '' and thisZipName.isdigit()):
        insertCommand = "insert into incidents (zipcode) values("+str(thisZipName)[:5]+");"
        #print insertCommand
        cur.execute(insertCommand)
'''
db.commit()
db.close()
