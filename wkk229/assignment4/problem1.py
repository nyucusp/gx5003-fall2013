import MySQLdb
import csv

   
 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="wkk229", # your username
                       passwd="python", # your password
                       db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
cur = db.cursor()  
 
 #creating tables
 #create borough table
createCommand = "create table borough (BoroughId int not null, zipcode int, BoroughName varchar(255), primary key(BoroughId))"
cur.execute(createCommand)
lines =  open('boroughs.csv').readlines()
idCounter = 0
for line in lines:
    columns = line.strip().split(',')

    zipcode = columns[0]
    name = columns[1]
    insertCommand = "insert into borough values(" + str(idCounter) + "," + str(zipcode) + "," + "'" + name + "'" + ");"
    cur.execute(insertCommand)
    idCounter +=1

# creating zipCode table
lines =  open('zipCodes.csv').readlines()
header = lines.pop(0).strip().split(',')

createCommand = "create table zipcodes (ZipcodeId int not null, Name varchar(255), ZipcodeTab varchar(255), Area varchar(255), PopPerZip int, primary key(ZipcodeId))"
cur.execute(createCommand)

for line in lines:
    columns = line.strip().split(',')

    name = columns[0]
    zipTab = columns[1]
    area = columns[7]
    if columns[10]:
        pop = int(columns[10])
    else:
        pop = 0
    insertCommand = "insert into zipcodes values(" + str(idCounter) + "," + "'" + name + "'" + "," + "'" + zipTab + "'" + "," + "'" + str(area) + "'" + "," + str(pop) + ");"
    cur.execute(insertCommand)
    idCounter +=1

# creating Incident table
lines =  open('incidents.csv').readlines()
header = lines.pop(0).strip().split(',')

createCommand = "create table incidents (IncidentId int not null, Address varchar(500), Zipcode varchar(255), IncidentKey int, primary key(IncidentId))"
cur.execute(createCommand)

for line in lines:
    columns = line.strip().rsplit(',', 2)
    add = columns[0].replace("'", "")
    zipcode = columns[1].replace("'", "")
    incKey = columns[2]
    insertCommand = "insert into incidents values(" + str(idCounter) + "," + "'" + add + "'" + "," + "'" + zipcode + "'" + ","  + str(incKey) + ");"
    cur.execute(insertCommand)
    idCounter +=1

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()

#stop the warnings from appearing from the drop if it exists
