import MySQLdb
import sys
from string import maketrans

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="wkk229", # your username
                       passwd="python", # your password
                       db="coursedb") # name of the data base

#The Cursor object will let you execute the sql commands
cur = db.cursor()

query = "select distinct i.Address from coursedb.borough b join coursedb.incidents i on i.Zipcode = b.zipcode where b.BoroughName in ('Queens', 'Bronx')"
cur.execute(query)

intab = "(),'"
outtab = "    "
trantab = maketrans(intab, outtab)
addresses = []
print "Addresses where incidents occurred in Manhattan the Bronx or Queens in the file BXQNAddressesWithIncidents.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(trantab)
    addresses.append(string.strip())
    string = ""


outFile = open("BXQNAddressesWithIncidents.txt", "w")
print >> outFile , "Addresses where incidents occurred in either the Bronx or Queens: \n"
for a in addresses:
    print >> outFile, a

outFile.close()

# close connection
db.close()
