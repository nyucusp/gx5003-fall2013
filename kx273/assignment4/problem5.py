import MySQLdb

 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 #The Cursor object 
cur = db.cursor()  
createCommand="select incident_address from incidents,boroughs where incidents.incident_zip=boroughs.zipcode and (boroughs.borough='Bronx' or boroughs.borough='Queens') "
cur.execute(createCommand)

for row in cur.fetchall():
    if row[0].strip()!="":
        print row[0]

 # commit the changes before closing connection. 
db.commit()	
 #close connection
db.close()
