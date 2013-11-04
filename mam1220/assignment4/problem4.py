# !usr/bin/python

######################################################################
#																	
# Assignment 3 - Problem 4
# November 2nd, 2013
#
# Michael Musick
#
#	Description: MySQL statement to 
#				"List addresses of all incidents that occurred in Manhattan.""
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import MySQLdb

#-------------------------------------------------------------------#
# --CONNECT TO THE MYSQL DB--
db = MySQLdb.connect(	host   = "localhost",# your host, usually localhost
						user   = "mam1220",  # your username
						passwd = "musick",   # your password
						db     = "coursedb") # name of the data base  
# create a cursor object to execute commands
cur = db.cursor()

query = "SELECT address FROM incidents_by_address I, boroughs B WHERE I.zip=B.zip AND B.borough=\'Manhattan\';"
cur.execute(query)
addressList = cur.fetchall()

for row in addressList:
	print row[0]