import MySQLdb

#connect to database

db = MySQLdb.connect(host = 'localhost', user = 'ks2890', passwd = '12345', db = 'coursedb')

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# Query all rows where age < 25
query = "select * from test where age <25"
cur.execute(query)

# Process the result. Here I am just printing out the rows

for row in cur.fetchall():
	# I already knwo 0th and 2nd columns are intergers, so i am converting them to string
	print str(row[0]) + " " + row[1] + " " + str(row[2])

# Close connection
db.close()