import sys
import MySQLdb
import warnings

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="efm279", # your username
                      passwd="password", # your password
                      db="coursedb") # name of the data base

#

# The Cursor object will let you execute the sql commands
cur = db.cursor()
userboro = sys.argv[1]
#userboro='Staten'

warnings.filterwarnings('ignore', category=MySQLdb.Warning)

countincident="SELECT SUM(coursedb.incidents.uniquekey) FROM (SELECT DISTINCT coursedb.boroughs.zip \
from coursedb.boroughs WHERE coursedb.boroughs.bname='"+userboro+"') z, coursedb.incidents WHERE \
coursedb.incidents.zip=z.zip;"

cur.execute(countincident)

for row in cur.fetchall() :
 	# I already know 0th and 2nd columns are integers, so i am converting them to string
 
     if str(row[0])=='None':
          print "zip code cannot be found"
     else:     
          count=row[0]


sumpopulation="SELECT sum(j.population)  FROM (SELECT DISTINCT \
coursedb.boroughs.zip from coursedb.boroughs WHERE coursedb.boroughs.bname='"+str(userboro)+"') z,\
coursedb.zipcodes j WHERE j.zip=z.zip;"

cur.execute(sumpopulation)

for row2 in cur.fetchall() :
 	# I already know 0th and 2nd columns are integers, so i am converting them to string
 
     if str(row2[0])=='None':
          print "zip code cannot be found"
     else:     
          print "number of inc. to population ratio for "+userboro+" is "+ str(count/row2[0]) 

# You must commit the changes before closing connection. Else the data would not be inserted.
db.commit() 
# close connection
db.close()
