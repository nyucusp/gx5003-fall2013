import MySQLdb
import sys

#taking the input
ZipIn = sys.argv[1]
#connect to database

db = MySQLdb.connect(host = 'localhost', user = 'ks2890', passwd = '12345', db = 'coursedb')

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# Query all rows where age < 25
query = "SELECT pop/area AS density  FROM zipCodes WHERE zipcode = %s;"
#query = "SELECT pop/area AS density FROM zipCodes;"
cur.execute(query,(ZipIn,))

# Process the result. Here I am just printing out the rows

for row in cur.fetchall():
	# I already know 0th and 2nd columns are intergers, so i am converting them to string
	print str(row)

# Close connection
db.close()