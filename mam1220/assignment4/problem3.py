# !usr/bin/python

######################################################################
#																	
# Assignment 3 - Problem 3
# November 2nd, 2013
#
# Michael Musick
#
#	Description: return ratio of incidents to population for a borough
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import MySQLdb
import sys


#-------------------------------------------------------------------#
# --CONNECT TO THE MYSQL DB--
db = MySQLdb.connect(	host   = "localhost",# your host, usually localhost
						user   = "mam1220",  # your username
						passwd = "musick",   # your password
						db     = "coursedb") # name of the data base  
# create a cursor object to execute commands
cur = db.cursor()
# try and get the user input then see if it is valid
query = "SELECT DISTINCT borough FROM boroughs;"
cur.execute(query)
boroughList = []
for row in cur.fetchall():
	boroughList.append(row[0])
try:
	# GET THE INPUT
	user_borough = sys.argv[1]
	if user_borough not in boroughList:
		raise MyError()
except:
	msg = "ERROR: Please enter a borough in the database -- " + str(boroughList)
	print msg
	print "Example \"python problem3.py Manhattan\""

	
#-------------------------------------------------------------------#
# -- GET THE NUMBER OF INCIDENTS AND POPULATION FOR THE BOROUGH--
query = "SELECT COUNT(address) FROM incidents_by_address I, boroughs B WHERE B.zip = I.zip AND B.borough=\'" + user_borough + "\';"
cur.execute(query)
for row in cur.fetchall():
	numOfIncidents = row[0]
	# print numOfIncidents
query = "SELECT SUM(population) FROM boroughs B, zip_infos Z WHERE B.zip = Z.zip AND B.borough = \'" + user_borough + "\';"
cur.execute(query)
for row in cur.fetchall():
	popOfZip = row[0]
	# print popOfZip

# compute the ratio
ratio = numOfIncidents / popOfZip
ratio = round( ratio * 1000 ) / 1000
print
print user_borough + " has a " + str(ratio) + " incidents per person ratio."
print