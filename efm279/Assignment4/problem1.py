import MySQLdb
import csv
import warnings

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="efm279", # your username
                      passwd="password", # your password
                      db="coursedb") # name of the data base  
# The Cursor object will let you execute the sql commands
cur = db.cursor()  
csv_data = csv.reader(file('boroughs.csv'))


warnings.filterwarnings("ignore", "Unknown table.*")

drop_query="DROP table IF EXISTS coursedb.boroughs"
cur.execute(drop_query)
drop_query2="DROP table IF EXISTS coursedb.zipcodes"
cur.execute(drop_query2)
drop_query3="DROP table IF EXISTS coursedb.incidents"
cur.execute(drop_query3)

# crete a table with 
createCommand = "create table boroughs (id int UNIQUE AUTO_INCREMENT, zip int not null, bname varchar(9), primary key(id))"
cur.execute(createCommand)
# Insert the csv_reader file using as strings in sql
for row in csv_data:
    
    # create command to insesrt this into the table
    #insertCommand = "insert into boroughs values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
    cur.execute('insert into boroughs (''zip'',''bname'') values (%s,%s)',row)
 
csv_data2 = csv.reader(file('zipCodes.csv'))
 
# crete a table with three attributes
createCommand2 = "create table zipcodes (id int UNIQUE AUTO_INCREMENT, name varchar(10) not null, zip varchar(30) not null, \
zt36d00 varchar(30) not null, perimeter varchar(11) not null, lsadtr varchar(12) not null,zt36d00i varchar(10) not null, \
lsad varchar(5) not null,area varchar(11), latitude varchar(15), longitude varchar(15), population varchar(30), primary key(id))"
cur.execute(createCommand2)
#Now we will insert 10 rows into this table
for row in csv_data2:
    
    # create command to insesrt this into the table
    #insertCommand = "insert into boroughs values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
    cur.execute('insert into zipcodes (''name'',''zip'',''zt36d00'',''perimeter'',''lsadtr'',''zt36d00i'',''lsad'',''area'',''latitude'',''longitude'',''population'') values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)

csv_data3 = csv.reader(file('Incidents_grouped_by_Address_and_Zip.csv'))
 
# crete a table with three attributes
createCommand3 = "create table incidents (id int UNIQUE AUTO_INCREMENT, address varchar(100) , zip varchar(30), \
uniquekey varchar(12) not null, primary key(id))"
cur.execute(createCommand3)
#Now we will insert 10 rows into this table
for row in csv_data3:
    
    # create command to insesrt this into the table
    #insertCommand = "insert into boroughs values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
    cur.execute('insert into incidents (''address'',''zip'',''uniquekey'') values (%s,%s,%s)',row)

delhead1='DELETE FROM coursedb.zipcodes WHERE coursedb.zipcodes.id=1'
delhead2='DELETE FROM coursedb.incidents WHERE coursedb.incidents.id=1'

cur.execute(delhead1)
cur.execute(delhead2)

repn1='UPDATE coursedb.zipcodes SET coursedb.zipcodes.population = NULL WHERE coursedb.zipcodes.population = "''"'
repn2='UPDATE coursedb.zipcodes SET coursedb.zipcodes.area = NULL WHERE coursedb.zipcodes.area = "''"'
repn3='UPDATE coursedb.incidents SET coursedb.incidents.address = NULL WHERE coursedb.incidents.address = "''" OR coursedb.incidents.address = "''ANONYMOUS''" OR coursedb.incidents.address = "''UNKNOWN''" OR coursedb.incidents.address = "''N/A''"'


cur.execute(repn1)
cur.execute(repn2)
cur.execute(repn3)

repn4='UPDATE coursedb.incidents SET coursedb.incidents.zip = NULL WHERE coursedb.incidents.zip = "''" OR coursedb.incidents.zip ="''XXXXX''"'
repn5='UPDATE coursedb.incidents SET coursedb.incidents.uniquekey = NULL WHERE coursedb.incidents.uniquekey = "''"'

cur.execute(repn4)
cur.execute(repn5)

repn6='UPDATE coursedb.incidents SET coursedb.incidents.zip=LEFT(coursedb.incidents.zip,5)'
cur.execute(repn6)

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
