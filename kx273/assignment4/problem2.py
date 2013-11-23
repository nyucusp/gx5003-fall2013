import MySQLdb
import sys

zipcode=str(sys.argv[1])
 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 #The Cursor object 
cur = db.cursor()  
createCommand="select sum(total_population_per_zip_code)/sum(area) from zipcodes where name="+"'"+zipcode+"'"
cur.execute(createCommand)

try:
    output= float(cur.fetchall()[0][0])
    print "Population density of "+zipcode+" is:";
    print output
except:
    print "ZIP cannot be found"

 # commit the changes before closing connection. 
db.commit()	
 #close connection
db.close()
