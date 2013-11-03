# !usr/bin/python

######################################################################
#																	
# Assignment 3 - Problem 6
# November 2nd, 2013
#
# Michael Musick
#
#	Description: MySQL statement to 
#				"List the set of zip codes in Manhattan along with ...
#				... their population where incidents have occurred."
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

query = "SELECT DISTINCT Z.zip, Z.population "
query += "FROM zip_infos Z, incidents_by_address I, boroughs B "
query += "WHERE B.borough='Manhattan' AND I.zip=B.zip AND Z.zip=I.zip "
query += "ORDER BY Z.zip;"

# print query

cur.execute( query )
returnedList = cur.fetchall()

for row in returnedList:
	print "zip code: " + str(row[0]) + " popultion: " + str(row[1])