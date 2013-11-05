#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 1
#Connects to MySQL and creates three tables to store the boroughs.csv, zipCodes, and incidents table. 


import MySQLdb
import csv


def incidentsToSql(cur,db):

	incidents_csv = csv.reader(open('Incidents_grouped_by_Address_and_Zip.csv'))
	rows = list(incidents_csv)
	rows = rows[1:]

	table = 'incidents'

	#make sure to set as root global max_allowed_packet=30000000; 
	query1 = "DROP TABLE IF EXISTS `{0}`;".format(table)
	query2 = "CREATE TABLE `{0}` (incident_address varchar(255) DEFAULT NULL, incident_zip varchar(255) DEFAULT NULL, unique_key INT DEFAULT NULL);".format(table)
	query3 = '''INSERT INTO `incidents` VALUES(%s, %s, %s)'''


	cur.execute(query1)
	db.commit()
	cur.execute(query2)
	db.commit()
	
	cur.executemany('''INSERT INTO `incidents` VALUES(%s, %s, %s)''', rows)
	db.commit()

def boroughToSql(cur,db):

	boroughs_csv = csv.reader(open('boroughs_tr.csv'))
	boroughs_rows = list(boroughs_csv)


	table2 = 'boroughs'


	query4 = "DROP TABLE IF EXISTS `{0}`;".format(table2)
	query5 = "CREATE TABLE `{0}` (zipcode varchar(255) DEFAULT NULL, borough varchar(255) DEFAULT NULL);".format(table2)


	cur.execute(query4)
	db.commit()
	cur.execute(query5)
	db.commit()

	cur.executemany('''INSERT INTO boroughs VALUES(%s, %s)''', boroughs_rows)
	db.commit()

def zipcodeToSql(cur,db):

	zipcodes_csv = csv.reader(open('zipcodes_tr.csv'))
	zipcode_rows = list(zipcodes_csv)
	zipcode_rows = zipcode_rows[1:]

	table3 = 'zipcodes'

	query6 = "DROP TABLE IF EXISTS `{0}`;".format(table3)
	query7 = "CREATE TABLE `{0}` (name varchar(255) DEFAULT NULL, zip_code_tabulation_area varchar(255) DEFAULT NULL, zt36_d00 varchar(255) DEFAULT NULL, perimeter varchar(255) DEFAULT NULL, lsad_trans varchar(255) DEFAULT NULL, zt36_d00i varchar(255) DEFAULT NULL, lsad varchar(255) DEFAULT NULL, area varchar(255) DEFAULT NULL, latitude varchar(255) DEFAULT NULL, longitude varchar(255) DEFAULT NULL, Total_Population_per_ZIP_Code varchar(255) DEFAULT NULL);".format(table3)


	cur.execute(query6)
	db.commit()
	cur.execute(query7)
	db.commit()

	cur.executemany('''INSERT INTO zipcodes VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', zipcode_rows)
	db.commit()


def main():
	#connect to database
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base
	
	cur = db.cursor()
	incidentsToSql(cur,db)

	boroughToSql(cur,db)

	zipcodeToSql(cur,db)
	db.close()
	print "Import complete"


if __name__ == "__main__":
	main()


