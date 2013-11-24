#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 4, Problem 4
#Connects to MySQL and returns a list of addresses of all incidents that occurred in Manhattan.

import MySQLdb
import sys


def main():

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
	                  user="jwr300", # your username
	                   passwd="jwr300", # your password
	                   db="coursedb") # name of the data base


	query = "SELECT DISTINCT incident_address FROM incidents JOIN boroughs WHERE borough = 'Manhattan' AND boroughs.zipcode = incidents.incident_zip;"

	cur = db.cursor()
	cur.execute(query)

	for row in cur.fetchall():
		print row[0]


	db.close()

if __name__ == "__main__":
	main()