import sys
import MySQLdb
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="efm279", # your username
                      passwd="password", # your password
                      db="coursedb") # name of the data base

#

# The Cursor object will let you execute the sql commands
cur = db.cursor()
userzip = sys.argv[1]
#userzip=10001

popdenq="SELECT sum(a.population)/sum(a.area) FROM (SELECT coursedb.zipcodes.population, coursedb.zipcodes.area FROM coursedb.zipcodes WHERE coursedb.zipcodes.zip="+str(userzip)+") a;"

cur.execute(popdenq)

for row in cur.fetchall() :
 	# I already know 0th and 2nd columns are integers, so i am converting them to string
 
     if str(row[0])=='None':
          print "zip code cannot be found"
     else:     
          print "population density for "+str(userzip)+" "+ str(row[0]) 

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()

