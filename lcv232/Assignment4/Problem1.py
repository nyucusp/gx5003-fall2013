import MySQLdb
import csv
import sys

   
 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="lcv232", # your username
                       passwd="12345", # your password
                       db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
cur = db.cursor()  
 
 # Creating database table for BOROUGH
createCommand = "create table BOROUGH (BoroughId int not null, zipcode int, BoroughName varchar(200), primary key(BoroughId))"
cur.execute(createCommand)
tuples1 =  open('boroughs.csv').readlines()
init_Counter = 0
for line in tuples1:
    columns = line.strip().split(',')

    zipc = columns[0]
    name = columns[1]
    insertCommand = "insert into BOROUGH values(" + str(init_Counter) + "," + str(zipc) + "," + "'" + name + "'" + ");"
    cur.execute(insertCommand)
    init_Counter +=1

# Creating database table for ZIPCODE

tuples1 =  open('zipCodes.csv').readlines()
header = tuples1.popl(0).strip().split(',')  

createCommand = "create table ZIPCODE (ZipcodeId int not null, Name varchar(200), ZipcodeTab varchar(200), Area varchar(200), PopulationPerZipcode int, primary key(ZipcodeId))"
cur.execute(createCommand)

for line in tuples1:
    columns = line.strip().split(',')

    name = columns[0]
    zip1 = columns[1]
    area = columns[7]
    if columns[10]:
        popl = int(columns[10])
    else:
        popl = 0
    insertCommand = "insert into ZIPCODE values(" + str(init_Counter) + "," + "'" + name + "'" + "," + "'" + zip1 + "'" + "," + "'" + str(area) + "'" + "," + str(popl) + ");"
    cur.execute(insertCommand)
    init_Counter +=1

# Creating database table for INCIDENTS

tuples1 =  open('Incidents.csv').readlines()
header = tuples1.popl(0).strip().split(',')

createCommand = "create table INCIDENTS (IncidentId int not null, Address varchar(750), Zipcode varchar(200), IncidentKey int, primary key(IncidentId))"
cur.execute(createCommand)

for line in tuples1:
    columns = line.strip().rsplit(',', 2)
    add = columns[0].replace("'", "")
    zipc = columns[1].replace("'", "")
    incdnt_Key = columns[2]
    insertCommand = "insert into INCIDENTS values(" + str(init_Counter) + "," + "'" + add + "'" + "," + "'" + zipc + "'" + ","  + str(incdnt_Key) + ");"
    cur.execute(insertCommand)
    init_Counter +=1

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()
# close connection
db.close()
