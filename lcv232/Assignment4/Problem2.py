import MySQLdb
import sys

ZipC_1 = sys.argv[1]  

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="lcv232", # your username
                   passwd="12345", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()
query = "select PopultionPerZipcode, Area from coursedb.ZIPCODE where ZipCodeTab = " + ZipC_1 + ""
cur.execute(query)
Popl_Overall = 0
Area_Overall = 0.0
for row in cur.fetchall() :
    Popl_Overall += row[0]
    Area_Overall += float(row[1])

print "Population Density for Zipcode " + ZipC_1 + ": " + str(Popl_Overall / Area_Overall)
# close connection
db.close()
