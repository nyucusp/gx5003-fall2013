import MySQLdb
   
#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rad416", # your username
                       passwd="mysql", # your password
                       db="coursedb") # name of the data base
 
# The Cursor object will let you execute the sql commands
cur = db.cursor()  
 
# query all rows were age < 25
query = "SELECT * FROM test WHERE age < 25"
cur.execute(query)

#process the result
for row in cur.fetchall():
  print str(row[0]) + " " + row[1] + " " + str(row[2])

#close connection
db.close()