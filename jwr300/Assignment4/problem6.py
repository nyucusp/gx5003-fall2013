#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 6
#Connects to MySQL and returns a list of the set of zip codes in Manhattan along with their population where incidents have occurred.

import MySQLdb
import sys


def main():

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base


	query = "SELECT DISTINCT name, Total_Population_per_ZIP_Code FROM zipcodes join boroughs WHERE borough = 'Manhattan' AND boroughs.zipcode = zipcodes.name;"

	cur = db.cursor()
	cur.execute(query)

	for row in cur.fetchall():
		print row[0], row[1]


	db.close()

if __name__ == "__main__":
	main()