#Problem 1 - create 3 tables & populate from csv files

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost",user="cnl272",passwd="p00p00",db="coursedb")
cur = db.cursor()
cur.execute("drop table if exists boroughs")
createCommand = "create table boroughs (zip varchar(255), borough_name varchar(255), primary key(zip));"
cur.execute(createCommand)

boroughs_file = open('boroughs.csv', 'r')
boroughs_lines = []
for line in boroughs_file:
	boroughs_lines.append(line)
boroughs_file.close()

for b in range(0,len(boroughs_lines)):
	borough_name = boroughs_lines[b].split(',')[1][:-1]
	borough_zipcode = boroughs_lines[b].split(',')[0]
	insertCommand = "insert into boroughs values("+ "'"+borough_zipcode+"'"+","+"'"+borough_name+"'"+")"+"ON DUPLICATE KEY UPDATE"+" zip="+borough_zipcode+";"
	cur.execute(insertCommand)
db.commit()

cur.execute("drop table if exists zipcodes")
createCommand = "create table zipcodes(zip varchar(255), area decimal(11,10), population int);"
cur.execute(createCommand)
zipCodes_file = open('zipCodes.csv', 'r')
zipCodes_lines = []
for line in zipCodes_file:
	zipCodes_lines.append(line[:-1])
zipCodes_file.close()

for z in range(1,len(zipCodes_lines)):
	zipcodes=zipCodes_lines[z].split(',')[0]
	area=float(zipCodes_lines[z].split(',')[7])
	population=zipCodes_lines[z].split(',')[10]
	if population != '':
		insertCommand="insert into zipcodes values("+"'"+zipcodes+"'"+","+str(area)+","+str(population)+");"
		cur.execute(insertCommand)
db.commit()

cur.execute("drop table if exists incidents")
createCommand = "create table incidents(zip varchar(255), address varchar(500), incidents_num int);"
cur.execute(createCommand)
incidents_file = open('incidents.csv', 'r')
incidents_line = []
for line in incidents_file:
	incidents_line.append(line)
incidents_file.close()

for i in range(1, len(incidents_line)):
	incident_zipcode=incidents_line[i].split(',')[1][0:5]
	if incident_zipcode.isdigit():
		incidents_address=incidents_line[i].split(',')[0].replace("'"," ")
		incidents_num=incidents_line[i].split(',')[2][:-1]
		if incidents_num.isdigit():
			insertCommand="insert ignore into incidents values("+"'"+incident_zipcode+"'"+","+"'"+incidents_address+"'"+","+incidents_num+");"
			cur.execute(insertCommand)
			
db.commit()
db.close()