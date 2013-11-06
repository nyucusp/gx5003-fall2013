import MySQLdb
import sys
from string import maketrans


#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="wkk229", # your username
                   passwd="python", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands

cur = db.cursor()
query = "select distinct i.Address from coursedb.borough b join coursedb.incidents i on i.Zipcode = b.zipcode where b.BoroughName = 'Manhattan'"
cur.execute(query)

#List addresses of all incidents that occurred in Manhattan.
intab = "(),'"
outtab = "    "
trantab = maketrans(intab, outtab)
addresses = []
print "Addresses where incidents occurred in Manhattan are in the file ManhattanAddressesWithIncidents.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(trantab)
    addresses.append(string.strip())
    string = ""


outFile = open("ManhattanAddressesWithIncidents.txt", "w")
print >> outFile , "Addresses where incidents occurred in Manhattan: \n"
for a in addresses:
    print >> outFile, a

outFile.close()

# close connection
db.close()
