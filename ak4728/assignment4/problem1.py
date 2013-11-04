import MySQLdb
import csv
import time

t0 = time.clock()
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="ak4728", # your username
                   passwd="password", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()  

def createTable(tablename,variable):
    try:
        dropTableIfExist = "DROP TABLE IF EXISTS " + tablename
        cur.execute(dropTableIfExist)
    except MySQLdb.Warning:
        pass
    createCommand = "create table " + tablename +' '+ variable
    cur.execute(createCommand)

def putNull(data,insert):
    for row in data:
        row = list(row)
        for i in range(0,len(row)):
            if row[i] == '' or row[i]=='ANONYMOUS' or row[i]=='NO CLUE' or row[i]=='NO IDEA' or row[i]=="DON'T KNOW" or row[i]=='IDK' or row[i]=='N/A' or row[i]=='NA' or row[i]=='N//A' or row[i]=='XXXXX' or row[i]=='XXX' or row[i]=='X' or row[i]=='NOT SURE' or row[i]=='UNKNOWN' or row[i]=='UNK' or row[i]=='X': #is the column value NULL?
                row[i] = None
        cur.execute(insert,row)

def insertData(filename, insert):
    csv_data = csv.reader(file(filename))
    next(csv_data)
    putNull(csv_data,insert)

# crete a table with three attributes
file1 = 'zipCodes.csv'
variable = "(name varchar(100), zipcode varchar(55), zt36 int not null, perim long, zcta varchar(100), zt36d int, lsad varchar(55), area long, lati long, longi long, popper varchar(55))"
insert = "INSERT INTO zipcode(name, zipcode, zt36, perim, zcta, zt36d, lsad, area, lati, longi, popper) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
createTable("zipcode",variable)
insertData(file1,insert)

file2 = 'Incidents_grouped_by_Address_and_Zip.csv'
variable2 = "(address varchar(255), zipcode varchar(50), uniquekey int not null)"
insert2 = "INSERT INTO incidents(address, zipcode, uniquekey) VALUES(%s, %s, %s)"
createTable("incidents",variable2)
insertData(file2,insert2)

file3 = 'boroughs.csv'
variable3 = "(zipcode varchar(50), borough varchar(255))"
insert3 = "INSERT INTO boroughs(zipcode, borough) VALUES(%s, %s)"
createTable("boroughs",variable3)
insertData(file3,insert3)


# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()

# close connection
db.close()

t1 = time.clock()

timex = t1-t0

print 'Done in ' + str(timex) + ' seconds'
