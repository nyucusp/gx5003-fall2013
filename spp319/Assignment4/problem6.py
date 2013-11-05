import MySQLdb
import sys
from string import maketrans

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="spp319", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base

#The Cursor object will let you execute the sql commands
cur = db.cursor()

query = "select distinct b.zipcode, z.PopPerZip from coursedb.borough b join coursedb.zipcodes z on z.ZipcodeTab = b.zipcode where b.BoroughName = 'Manhattan' and b.zipcode in (select zipcode from coursedb.incidents)"
cur.execute(query)

intab = "(),'L"
outtab = "     "
trantab = maketrans(intab, outtab)
addresses = []
print "Manhattan zipcodes and the corresponding populations where incidents have occurred are in the file ManhattanZipPop.txt"
string = ""
for row in cur.fetchall():
    string = str(row)
    string = string.translate(trantab)
    addresses.append(string.strip())
    string = ""


outFile = open("ManhattanZipPop.txt", "w")
print >> outFile , "Zipcodes and the corresponding Populations where incidents have occurred in Manhattan: \n"
for a in addresses:
    print >> outFile, a

outFile.close()

# close connection
db.close()
