#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 3
#Connects to MySQL and computes the ratio between number of incidents and population for a given borough

import MySQLdb
import sys


def main():
	inputBorough = sys.argv[1]

	if inputBorough == "Staten Island":
		inputBorough = "Staten"

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base


	query = "SELECT sum(Total_Population_per_ZIP_Code) FROM boroughs join zipcodes WHERE borough = " + "'" + inputBorough + "'" + " AND boroughs.zipcode = zipcodes.name;"

	cur = db.cursor()
	cur.execute(query)
	total_pop = 0
	for row in cur.fetchall():
		total_pop += int(row[0])

	

	query2 = "SELECT sum(unique_key) FROM incidents join boroughs WHERE borough = " + "'" + inputBorough + "'" + " AND boroughs.zipcode = incidents.incident_zip;"
	cur.execute(query2)
	total_incidents = 0
	for row in cur.fetchall():
		total_incidents += int(row[0])


	print float(total_incidents)/float(total_pop)


	db.close()

if __name__ == "__main__":
	main()

