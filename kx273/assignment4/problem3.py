import MySQLdb
import sys

boro=str(sys.argv[1])
 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 #The Cursor object 
cur = db.cursor()  
createCommand="select sum(total_population_per_zip_code) from zipcodes,boroughs where zipcodes.name=boroughs.zipcode and boroughs.borough="+"'"+boro+"'"
cur.execute(createCommand)
population=cur.fetchall()[0][0]

createCommand="select count(*) from incidents,boroughs where incidents.incident_zip=boroughs.zipcode and boroughs.borough="+"'"+boro+"'"
cur.execute(createCommand)
incidentNum=cur.fetchall()[0][0]

try:
    incidentRate=float(incidentNum)/float(population)
    print "The incident rate of "+boro+" is:";
    print incidentRate
except:
    print "Borough given cannot be found!"


 # commit the changes before closing connection. 
db.commit()	
 #close connection
db.close()
