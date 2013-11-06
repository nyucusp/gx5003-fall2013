#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 5
#Connects to MySQL and returns a list of addresses of all incidents that have occurred either in Bronx or Queens.

import MySQLdb
import sys

def main():

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base


	query = "SELECT DISTINCT i.incident_address FROM incidents i, boroughs b WHERE (b.borough = 'Queens' OR b.borough = 'Bronx') AND b.zipcode = i.incident_zip;"

	cur = db.cursor()
	cur.execute(query)

	for row in cur.fetchall():
		print row[0]


	db.close()

if __name__ == "__main__":
	main()