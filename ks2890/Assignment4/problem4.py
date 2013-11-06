import MySQLdb

#connect to database

db = MySQLdb.connect(host = 'localhost', user = 'ks2890', passwd = '12345', db = 'coursedb')

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# Query all rows where age < 25
query = "SELECT address FROM incidents, zipCodes, boroughs WHERE (zipCodes.zipcode = incidents.zipcode) AND (zipCodes.zipcode = boroughs.zipcode) AND borough = manhattan;"
cur.execute(query

# Process the result. Here I am just printing out the rows

for row in cur.fetchall():
	print str(row)

# Close connection
db.close()