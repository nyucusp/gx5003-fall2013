# !usr/bin/python

######################################################################
#																	
# Assignment 3 - Problem 1
# November 2nd, 2013
#
# Michael Musick
#
#	Description: Place the csv files into MySQL tables
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

cur.execute("SET autocommit = 0;")

# get all tables that currently exist in this db
query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'coursedb';"
cur.execute(query)
previousTables = []
for row in cur.fetchall():
	# print row[0]
	previousTables.append( row[0] )	


#-------------------------------------------------------------------#
# --BOROUGHS.CSV--

# create a table for the boroughs data to be stored in
# delete any old tables
if "boroughs" in previousTables:
	query = "DROP TABLE boroughs;"
	cur.execute(query)
	# print "table existed"
query = "CREATE TABLE boroughs ( zip MEDIUMINT UNSIGNED NOT NULL, borough VARCHAR(9), primary key(zip) );"
# print query
cur.execute(query)

# open the csv db file
csvFile = open('boroughs.csv', 'r')

# get the data from this file
# create a zip list for checking
zipList = []
for line in csvFile:
	tempArray = line.strip().split(',')
	
	zipCode = int( tempArray[0] )
	borough = tempArray[1]

	if zipCode not in zipList:
		zipList.append(zipCode)
		# create the insert query
		query = "INSERT INTO boroughs values(" + str(zipCode) + ", '" + str(borough) + "' );"
		# print query
		cur.execute(query)

# close the csv file
csvFile.close()


#-------------------------------------------------------------------#
# --ZIPCODES.CSV--

# create a table for the boroughs data to be stored in
# delete any old tables
if "zip_infos" in previousTables:
	query = "DROP TABLE zip_infos;"
	cur.execute(query)
	# print "table existed"
query = "CREATE TABLE zip_infos ( zip MEDIUMINT UNSIGNED NOT NULL, "
query += "area DECIMAL(13,9) UNSIGNED, population INT UNSIGNED, primary key(zip) );"
# print query
cur.execute(query)

# open the csv db file
csvFile = open('zipCodes.csv', 'r')
# go through that freaking document
for line in csvFile:
	# print line

	# complete entry flag
	completeEntry = True

	tempArray = line.strip().split(',')

	# if the zip is valid
	if( tempArray[1].isdigit()):
		# print tempArray[1]		
		# print tempArray

		# assign the zip to the variable
		zipCode = int(tempArray[1])
		# check if the zip code has an associated NYC borough from the last csv file
		# if not, then I am assuming it is not in NYC and not valid
		if zipCode not in zipList:
			completeEntry = False

		# this is the population for a given zip
		if( len(tempArray[10]) > 0  ):
			pop = int(tempArray[10])
		else:
			completeEntry = False

		# get the area
		if( len( tempArray[7] ) > 0 ):
			area = str( tempArray[7] )
		else:
			area = "0"

		if completeEntry:
			query = "INSERT INTO zip_infos values( " + str(zipCode) + ", '" + area + "', " + str(pop) + ");"
			cur.execute(query)

# close the csv file
csvFile.close()


#-------------------------------------------------------------------#
# --INCIDENTCS BY ADDRESS .CSV--

# create a table for the boroughs data to be stored in
# delete any old tables
if "incidents_by_address" in previousTables:
	query = "DROP TABLE incidents_by_address;"
	cur.execute(query)
	# print "table existed"
query = "CREATE TABLE incidents_by_address ( id INT AUTO_INCREMENT NOT NULL, zip MEDIUMINT UNSIGNED NOT NULL, "
query += "address VARCHAR(255), primary key(id) );"
# print query
cur.execute(query)

# open the csv db file
csvFile = open('IncidentsByAddress.csv', 'r')
# go through that freaking document
for line in csvFile:
	# print line

	# complete entry flag
	completeEntry = True

	tempArray = line.strip().split(',')

	# get the zip code
	if( tempArray[1].isdigit() and len(tempArray[1]) == 5 ):
		zipCode = int(tempArray[1])
	# if it is not a valid 5 digit number then the entry is not usable
	else: 
		completeEntry = False

	# get the address string
	address = str(tempArray[0])

	if completeEntry:
		query = "INSERT INTO incidents_by_address (zip, address) VALUES(" + str(zipCode) + ", \"" + address + "\");"
		# print query
		cur.execute(query)	

# close the csv file
csvFile.close()



#-------------------------------------------------------------------#
# COMMIT AND CLOSE ALL REMAINING CONNECTIONS
db.commit()
db.close()