import MySQLdb
import sys
from string import maketrans


#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="lcv232", # your username
                   passwd="12345", # your password
                   db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands

cur = db.cursor()
query = "select distinct i.Address from coursedb.BOROUGH b join coursedb.INCIDENTS i on i.Zipcode = b.zipcode where b.BoroughName = 'Manhattan'"
cur.execute(query)

#Listing all the addresses of the Incidents that occured in the Borough Manhattan.
intab = "(),'"
outtab = "    "
transfer1 = maketrans(intab, outtab)
address = []
print "Listing all the Addresses where the Incidents occurred in the Borough Manhattan are in the file ManhattanAddressesWithIncidents.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(transfer1)
    address.append(string.strip())
    string = ""


outputFile = open("ManhattanAddressesWithIncidents.txt", "w")
print >> outputFile , " Data of Addresses where Incidents occurred in the Borough Manhattan: \n"
for a in address:
    print >> outputFile, a

outputFile.close()

# close connection
db.close()
