import MySQLdb
import sys

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="ak4728", # your username
                   passwd="password", # your password
                   db="coursedb") # name of the data base  
# The Cursor object will let you execute the sql commands
cur = db.cursor()

zip = sys.argv[1]

# Given a zip code as input in the command line, compute the population density of that zip code.
query = "SELECT sum(x.popper)/sum(x.area) FROM (SELECT coursedb.zipcode.popper,\
coursedb.zipcode.area FROM coursedb.zipcode WHERE coursedb.zipcode.zipcode=" + str(zip) + ") x;"
cur.execute(query)
# process the result. Here I am just printing out the rows

for row in cur.fetchall() :
    if row[0] == None:
        print "Zipcode is not in the list of zipcodes, try again."
    else:
        print 'The population density of ' + str(zip) + ' is ' + str(row[0])
    
# close connection
db.close()
