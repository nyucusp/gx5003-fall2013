import MySQLdb
import sys

#taking the input
BoroughIn = sys.argv[1]
#connect to database

db = MySQLdb.connect(host = 'localhost', user = 'ks2890', passwd = '12345', db = 'coursedb')

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# Query all rows where age < 25
query = "SELECT num_inc/pop  AS ratio  FROM incidents, zipCodes, boroughs WHERE (zipCodes.zipcode = incidents.zipcode) AND (zipCodes.zipcode = boroughs.zipcode) AND borough = %s;"
#query = "SELECT pop/area AS density FROM zipCodes;"
cur.execute(query,(BoroughIn,))

# Process the result. Here I am just printing out the rows

for row in cur.fetchall():
	print str(row)

# Close connection
db.close()