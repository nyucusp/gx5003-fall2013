import csv
import MySQLdb

 #connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
 # The Cursor object executes the sql commands
cur = db.cursor()  
 
 # create Boroughs table with relevant attributes in the Boroughs.csv file
createBoroughs = "create table Boroughs (zip varchar(5) not null, borough varchar(9))"
cur.execute(createBoroughs)
 # import data from Boroughs.csv file to Boroughs table 
queryBoroughs = """ LOAD DATA LOCAL INFILE 'boroughs.csv' INTO TABLE boroughs FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' Lines terminated by '\n' """ 
cur.execute(queryBoroughs)

# create Zipcodes tables with relevant attributes in the zipCodes.csv file
createZipcodes = "create table Zipcodes (name varchar(5) not null , zip_code_tabulation_area varchar(5), zt36_d00 varchar(10), perimeter varchar(11), lsad_trans varchar(12), zt36_d00_i varchar(4), lsad varchar(2),area varchar(11), latitute varchar(15), longitude varchar(15), Total_Population_per_ZIP_Code varchar(6))"
cur.execute(createZipcodes)
# import data from zipCodes.csv file to Zipcodes table 
queryZipcodes = """ LOAD DATA LOCAL INFILE 'zipCodes.csv' INTO TABLE Zipcodes FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' Lines terminated by '\n' IGNORE 1 LINES """ 
cur.execute(queryZipcodes)

# create Incidents tables with relevant attributes in the Incidents.csv file
createIncidents = "create table Incidents (Incident_Address varchar(80), Incident_Zip varchar(10) not null, Unique_Key int(6))"
cur.execute(createIncidents)
# import data from Incidents.csv file to Incidents table 
queryIncidents = """ LOAD DATA LOCAL INFILE 'Incidents.csv' INTO TABLE Incidents FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' Lines terminated by '\n' IGNORE 1 LINES """ 
cur.execute(queryIncidents)

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit()	
# close connection
db.close()
