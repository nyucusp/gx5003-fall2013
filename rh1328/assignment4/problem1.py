import MySQLdb
import csv   
import re

def parseAndAddBoroughsToDB(cur):
      	data = open("boroughs.csv", 'r')
	checkDup = False
      	for i, line in enumerate(data):
		line = line.strip()
		arr = line.split(',')
		zipcode = arr[0] 
		borough = arr[1]
		#set empty strings to null
		if zipcode == '':
			zipcode = 'NULL'
		if borough == '':
			borough = 'NULL'
		insertCommand = "insert into boroughs values(" + str(zipcode) + "," + "'" +  borough + "'" + ")" + "ON DUPLICATE KEY UPDATE" + " zipcode = " + zipcode + ";"
		print insertCommand
		cur.execute(insertCommand)
		

def parseAndAddIncidentsToDb(cur):
	data = open("Incidents_grouped_by_Address_and_Zip.csv", "r")
	columnHeader = True
	rowreader = csv.reader(data, delimiter=',', skipinitialspace=True)
	for line in rowreader:
		if columnHeader:
		    columnHeader = False
		    continue
		print line
		incidentAddress = line[0]
                
		print incidentAddress
		incidentZip = line[1]
		incidentAddress = str(MySQLdb.escape_string(str(line[0])))
		uniqueKey = line[2]
		#if one of the categories is an empty string, make it a Null value
		if incidentAddress == '' or incidentAddress == 'N/A' or incidentAddress == "not avail not avail" or incidentZip == "NA":
			incidentAddress = 'NULL' 
		if incidentZip == '' or incidentZip == 'N/A' or incidentZip == 'NY' or incidentZip == 'not avail not avail' or incidentZip == "NA" or incidentZip.isdigit() == False:
			incidentZip = 'NULL'
		if uniqueKey == '' or uniqueKey == 'N/A' or incidentZip == "not avail not avail" or incidentZip == "NA":
			uniqueKey = 'NULL'
		#print incidentAddress, incidentZip, uniqueKey
		insertCommand = "insert into incidents values(" + "'"+ incidentAddress +"'" +  "," + str(incidentZip) + "," + str(uniqueKey) + ");"
		print insertCommand
		cur.execute(insertCommand)


def parseAndAddZipcodesToDB(cur):
	data = open("zipCodes.csv", "r")
      	columnHeader = True
      	for line in data:
        	if columnHeader:
              		columnHeader = False
              		continue
        	line = line.strip()
          	arr = line.split(",")
          	zipcode = arr[0]
		#repeat of zipcode, dont use:
		repeatVal = arr[1]
		zt3600 = arr[2]
		perimeter = arr[3]
		lsadtrans = arr[4]
		zt3600i = arr[5]
		lsad = arr[6]
		area = arr[7]	
		latitude = arr[8]
		longitude = arr[9]
		population = arr[10]
		#set empty strings to be null
		if zipcode == '':
			zipcode = 'NULL' 
		if zt3600 == '':
			zt3600 = 'NULL'
		if perimeter == '':
			perimeter = 'NULL'
		if lsadtrans == '':
			lsadtrans = 'NULL' 
		if zt3600i == '':
			zt3600 = 'NULL'
		if lsad == '':
			lsad = 'NULL'
		if area == '':
			area = 'NULL' 
		if latitude == '':
			latitude = 'NULL'
		if longitude == '':
			longitude = 'NULL'
		if population == '':
			population = 'NULL'

	
		insertCommand = "insert into zipCodeData values(" + "'" + zipcode + "'" + "," + str(zt3600)  + "," + str(perimeter) + "," + "'" + lsadtrans + "'" + "," +  str(zt3600i) + "," +  "'" + lsad + "'" + "," +  str(area) + "," +  str(latitude) + "," + str(longitude) + "," +  str(population) + ");"
  		print insertCommand
		cur.execute(insertCommand)




def main():
	 #connect to database
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
			      user="rh1328", # your username
			       passwd="cusppassword", # your password
			       db="coursedb") # name of the data base
	 
	 # The Cursor object will let you execute the sql commands
	cur = db.cursor()  

	cur.execute("DROP TABLE IF EXISTS boroughs")
	cur.execute("DROP TABLE IF EXISTS zipCodeData")
	cur.execute("DROP TABLE IF EXISTS incidents")


	 
	createCommand1 = "create table boroughs (zipcode varchar(255) not null, boroughName varchar(255), primary key(zipcode))"
	cur.execute(createCommand1)
	parseAndAddBoroughsToDB(cur)

	#i chose to omit name and just use zip code tabulation area in the table because both have 
	#the same value for each entry in the dataset
	createCommand2 = "create table zipCodeData (zipcode varchar(255) not null, zt36d00 int, perimeter decimal(20,20), lsadtrans varchar(255), zt3600i int, lsad varchar(255), area decimal(20,20), latitude decimal(20,20), longitude decimal(20,20), population int, primary key(zt36d00))"
	cur.execute(createCommand2)
	parseAndAddZipcodesToDB(cur)

#MADE ZIPCODE A varchar  BECAUSE some zip codes have bad data - including letters in them
#THERE ARE NO UNIQUE PRIMARY KEYS EVEN WHEN USING ALL DATA AVAILABLE IN THIS TABLE, SO NO PRIMARY KEY IS MADE
	createCommand3 = "create table incidents (address varchar(255) not null, zipcode varchar(255), id int)"
	cur.execute(createCommand3)
	parseAndAddIncidentsToDb(cur)

	db.commit()
	db.close()


if __name__ == "__main__":
	main()
