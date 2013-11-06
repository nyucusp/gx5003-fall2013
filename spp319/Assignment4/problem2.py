import MySQLdb
import sys

givenZip = sys.argv[1]


#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="spp319", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()
query = "select PopPerZip, Area from coursedb.zipcodes where ZipcodeTab = " + givenZip + ""
cur.execute(query)
totalPop = 0
totalArea = 0.0
for row in cur.fetchall() :
    totalPop += row[0]
    totalArea += float(row[1])

print "Population Density for zip " + givenZip + ": " + str(totalPop / totalArea)
# close connection
db.close()
