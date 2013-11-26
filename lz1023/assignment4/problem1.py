import MySQLdb
#connect to database
db=MySQLdb.connect(host="localhost",
	               user="lz1023",
	               passwd="19600313",
	               db="coursedb")

cur=db.cursor()

#create a table borough with 3 attributes
createCommand="create table if not exists borough (zip varchar(255), name varchar(255), primary key(zip))"
cur.execute(createCommand)
#insert 3 rows into this table
myFile=open('boroughs.csv','r')
readdata=[]
for line in myFile:
	readdata.append(line[:-1])
myFile.close()

for i in range(0, len(readdata)):
	zipcode=readdata[i].split(',')[0]
	name=readdata[i].split(',')[1]	
	#create command to insert this into the table
	insertCommand="insert into borough values("+ "'" + zipcode + "'"+ "," +"'"+ name + "'" + ")"+"ON DUPLICATE KEY UPDATE" + " zip = " + zipcode + ";"
	cur.execute(insertCommand)


#create a table zipcodes with three attributes
createCommand="create table if not exists zipcodes (zip varchar(255), area decimal(11,10), population int)"
cur.execute(createCommand)
#insert 3 rows into this table
myFile=open('zipCodes.csv','r')
readdata=[]
firstline=0
for line in myFile:
	if firstline==0:
		firstline=1
	else:
		readdata.append(line[:-1])
myFile.close()

for i in range(0, len(readdata)):
	zipcode=readdata[i].split(',')[0]
	area=float(readdata[i].split(',')[7])
	population=readdata[i].split(',')[10]
	if population != '':
		insertCommand="insert into zipcodes values("+"'"+zipcode+"'"+","+str(area)+","+str(population)+");"
		cur.execute(insertCommand)


#create a table incidents with three attributes
createCommand="create table if not exists incidents (zip varchar(255), address varchar(255), incident_num int)"
cur.execute(createCommand)
#insert 3 rows into this table
myFile=open('Incidents_grouped_by_Address_and_Zip.csv','r')
readdata=[]
firstline=0
for line in myFile:
	if firstline==0:
		firstline=1
	else:
		readdata.append(line[:-1])
myFile.close()

for i in range(0, len(readdata)):
	zipcode=readdata[i].split(',')[1][:5]
	if zipcode.isdigit():
		address=readdata[i].split(',')[0].replace("'","")
		incident_num=readdata[i].split(',')[2]
		if incident_num.isdigit():
			insertCommand="insert into incidents values("+"'"+zipcode+"'"+","+"'"+address+"'"+","+str(incident_num)+");"
			cur.execute(insertCommand)

db.commit()
db.close	