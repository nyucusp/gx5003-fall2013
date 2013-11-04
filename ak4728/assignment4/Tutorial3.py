import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                  user="courseuser", # your username
                   passwd="password", # your password
                   db="coursedb") # name of the data base  
# The Cursor object will let you execute the sql commands
cur = db.cursor()   
# query all rows where age < 25
query = "select * from test where age < 25"
cur.execute(query)
# process the result. Here I am just printing out the rows
for row in cur.fetchall() :
    # I already know 0th and 2nd columns are integers, so i am converting them to string
 print str(row[0]) + " " + row[1] + " " + str(row[2])
# close connection
db.close()
