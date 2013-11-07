import MySQLdb

 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 #The Cursor object 
cur = db.cursor()  
createCommand="select zipcodes.name, sum(zipcodes.total_population_per_zip_code) from incidents,boroughs,zipcodes where incidents.incident_zip=zipcodes.name and boroughs.zipcode=zipcodes.name and boroughs.borough='Manhattan' group by zipcodes.name"
cur.execute(createCommand)

for row in cur.fetchall():
    print str(row[0])+'\t'+str(row[1])

 # commit the changes before closing connection. 
db.commit()	
 #close connection
db.close()
