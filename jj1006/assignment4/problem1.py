import MySQLdb
import csv
   
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="jj1006", # your username
                     passwd="jpwd", # your password
                     db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()  
 
# create a table for the boroughs 
createCommand = "create table boroughs (zip varchar(255) not null, borough varchar(255), primary key(zip))"
cur.execute(createCommand)
b = open('../assignment2/boroughs.csv','r')
for line in b:
	line = line.rstrip()
	zip = line.split(',')[0]
 	borough = line.split(',')[1]
 	insertCommand = "insert ignore into boroughs values('" + zip + "','"+ borough +"');"
 	cur.execute(insertCommand)
 
db.commit()	

# create a table for the zipCodes
createCommand = "create table zipCodes(zip varchar(255) not null, tabarea varchar(255), zt36 varchar(255), perimeter int, lsadtrans varchar(255), zt36i varchar(255), lsad varchar(255), area float, latitude float, longitude float, population int, primary key(zip))"
cur.execute(createCommand)
header=True
with open('../assignment2/zipCodes.csv','rb') as f:
	z = csv.reader(f)
	for row in z: 
		if not header: #filter out header
			row = ['NULL' if x=='' else x for x in row]
	        	cur.execute("insert ignore into zipCodes values('%s', '%s', '%s', %s, '%s', '%s', '%s', %s, %s, %s, %s);" %tuple(row))
		header=False

db.commit()

# create a table for the incidents
createCommand = "create table incidents(address varchar(255) not null, zip varchar(255), uk int, id int, primary key(id))"
cur.execute(createCommand)
id=0
with open('../assignment2/Incidents_grouped_by_Address_and_Zip.csv','rb') as f:
       z = csv.reader(f)
       for row in z:
               if not id==0: #filter out header
                       row = ['NULL' if x=='' else x for x in row]
		       row.append(id)
		       print "insert ignore into incidents values(\"%s\", \"%s\", %s, %s);" %tuple(row)
                       cur.execute("insert ignore into incidents values(\"%s\", \"%s\", %s, %s);" %tuple(row))
               id=id+1

db.commit()


# close connection
db.close()
