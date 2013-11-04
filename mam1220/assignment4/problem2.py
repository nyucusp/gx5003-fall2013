# !usr/bin/python

######################################################################
#																	
# Assignment 3 - Problem 2
# November 2nd, 2013
#
# Michael Musick
#
#	Description: return population density for a given zip
#
######################################################################

# IMPORT NECCESSARY LIBRARIES
import MySQLdb
import sys

# try and get the user input
try:
	# GET THE INPUT
	user_zip = sys.argv[1]
	if len(user_zip) != 5 or user_zip.isdigit() == False:
		raise MyError()
except:
	msg = "Please Enter a valid 5 digit zip code"
	print msg

#-------------------------------------------------------------------#
# --CONNECT TO THE MYSQL DB--
db = MySQLdb.connect(	host   = "localhost",# your host, usually localhost
						user   = "mam1220",  # your username
						passwd = "musick",   # your password
						db     = "coursedb") # name of the data base  
# create a cursor object to execute commands
cur = db.cursor()

query = "SELECT population, area FROM zip_infos WHERE zip=" + str(user_zip) + ";"
cur.execute(query)
returned = cur.fetchall()
if len(returned)==0:
	print
	print "supplied zip code is not in database..."
	print
else:
	returned = returned[0]
	# get the density = population / square size
	popDensity = returned[0] / returned[1]
	# round it
	popDensity = round(popDensity*1000) / 1000
	print
	print "Population Density for zip code " + str(user_zip) + " is " + str(popDensity) + " people per square mile."
	print