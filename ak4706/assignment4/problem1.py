import csv
import MySQLdb

db = MySQLdb.connect(host='localhost',
    user='ak4706',
    passwd='Atara7890',
    db = 'coursedb')
cursor = db.cursor()

#create table Borough 
cursor.execute("CREATE TABLE Borough(Zip int, Borough varchar(15))")
csv_data = csv.reader(file('boroughs.csv'))
for row in csv_data:
    cursor.execute('''Insert into Borough(Zip, Borough)
    				  Values (%s, %s)''', row)

#create table Zipcode
cursor.execute("CREATE TABLE `Zipcode`(Zip int not null, area float not null, pop int not null)")
csvzip = csv.reader(file('zipCodes.csv'))
zips = list(csvzip)[1:]
for row in zips:
	Zip = row[0]
	area = row[7]
	pop = row[10]
	if (Zip != '' and area !='' and pop !='' and Zip[3] != 'H' and Zip[3] != 'X'):
		cursor.execute("Insert into Zipcode(Zip, area, pop)\
  				           Values (%s, %s, %s)", (Zip, area, pop))

#create table incidents
cursor.execute("CREATE TABLE `Incidents`(Incadd varchar(255), Inczip int(5) not null, Incnum int(10) not null)")
csvinc = csv.reader(file('Incidents_grouped_by_Address_and_Zip.csv'))
inc = list(csvinc)[1:]
for row in inc:
	if(row[0] !='' and row[1] !='' and len(row[1])==5 and row[1]!='XXXXX' and row[2]!=''):
		Incadd= row[0]
		Inczip= int(row[1][0:5])
		Incnum = row[2]
		if (Incadd !='' and Inczip !='' and Incnum !='' and Inczip != 'N/A' and  Inczip != 'NY' and Inczip != 'NA' and Inczip != 'NJ 07' and Incadd != 'N/A'):
			#print Incadd
			#print Inczip
			cursor.execute("Insert into Incidents(Incadd, Inczip, Incnum)\
		 					Values (%s, %s, %s)", (Incadd, Inczip, Incnum))

#close the connection to the database.
db.commit()
cursor.close()
print "Done"