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
#userboro = sys.argv[1]
userboro='Manhattan'

addresses="SELECT coursedb.incidents.address from (select distinct coursedb.boroughs.zip from coursedb.boroughs where coursedb.boroughs.bname='Bronx' or 'Queens') z, \
coursedb.incidents WHERE coursedb.incidents.zip=z.zip  "

cur.execute(addresses)

for row in cur.fetchall() :
 	# I already know 0th and 2nd columns are integers, so i am converting them to string
 	print row[0]
 


# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
