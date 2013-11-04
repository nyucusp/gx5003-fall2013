BACKUP


#Nathan Seltzer
#Assignment 4
#Problem 1

import MySQLdb
  
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="seltzn01", # your username
                      passwd="inform", # your password
                      db="coursedb") # name of the data base

cur = db.cursor()  

#drop table if already exists
cur.execute("DROP TABLE IF EXISTS boroughs")
# create a table with three attributes
createBoroughs = ("create table boroughs (zipcode int, borough varchar(255), primary key(zipcode))")
cur.execute(createBoroughs)



# # Now we will insert 10 rows into this table
# for i in range(10):
# 	name = "name" + str(i)
# 	age = 20 + i
# 	# create command to insesrt this into the table
# 	insertCommand = "insert into test values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
# 	cur.execute(insertCommand)

cur.execute("DROP TABLE IF EXISTS incidents")
createIncidents = ("create table incidents (incident_address varchar(255), zipcode int, unique_key int, primary key(zipcode))")
cur.execute(createIncidents)


cur.execute("DROP TABLE IF EXISTS zipcodes")
createZipcodes = ("create table zipcodes (zipcode int, zipcode_tabulation_area int,zt36_d00 int, perimeter float, lsad_trans varchar(255), zt36_d00_i int, lsad varchar(255), area float, latitude float, longitude float, TotalPopulation int, primary key (zipcode))")
cur.execute(createZipcodes)




db.commit()	
# close connection
db.close()