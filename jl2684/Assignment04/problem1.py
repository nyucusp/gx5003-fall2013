import MySQLdb
import csv
import sys
 
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    user="jl2684", # your username
                    passwd="199900", # your password
                    db="coursedb") # name of the data base  


#open files 
borough_file = open('boroughs.csv', 'rb')
borough_lines = csv.reader(borough_file)

zip_code_file = open('zipCodes.csv', 'rb')
zip_code_lines = csv.reader(zip_code_file)

incident_file = open('Incidents_grouped_by_Address_and_Zip.csv', 'rb')
incident_lines = csv.reader(incident_file)

cur = db.cursor()   

# Get rid of first lines 
zip_code_lines_data =[]
for i in zip_code_lines:
	zip_code_lines_data.append(i)
incident_data =[]
for i in incident_lines:
	incident_data.append(i)


# Create borough table with two attributes 
createCommand = "create table borough (zipcode varchar(255), borough_name varchar(255))"
createCommand = "create table zipcode (zipcode varchar(255), population_of_zip varchar(255), area varchar(255))"
createCommand = "create table incidents (address varchar(255), zipcode varchar(255), incident varchar(255))"

cur.execute(createCommand)

# Create Tables 
for i in borough_lines:
	zipcode = str(i[0])
 	borough_name = str(i[1])
 	insertCommand = "insert into borough values(" + "'" + zipcode + "'" + "," + "'" + borough_name + "'" + ");"
 	cur.execute(insertCommand)


for i in zip_code_lines_data[1:]: 
	if str(i[1]).find('HH') == -1: 
		if str(i[10]) != '':
			zipcode = str(i[1])
			population_of_zip = str(i[10])
			area = i[7]
			insertCommand = "insert into zipcode values(" + "'" + zipcode + "'" + "," + "'" + population_of_zip + "'"+ "," + str(area) + ");"
		 	cur.execute(insertCommand)


for i in incident_data[1:]: 
	if str(i[1]) != '' and str(i[1]) != "DON'T KNOW":
		address = str(str(i[0]).replace("'", ""))
		zipcode = str(i[1][:5])
		incident = str(i[2])
		insertCommand = "insert into incidents values(" + "'" + address + "'" + "," + "'" + zipcode + "'" + "," + "'" + incident + "'" + ");"
		cur.execute(insertCommand)

db.commit()	
db.close()

borough_file.close 
zip_code_file.close 
incident_file.close 