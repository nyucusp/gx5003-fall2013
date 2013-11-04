import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="seltzn01", # your username
                      passwd="inform", # your password
                      db="coursedb") # name of the data base

# The Cursor object will let you execute the sql commands
cur = db.cursor()  

# crete a table with three attributes
Command = "create table what (id int, something varchar(255), numbers int, primary key(id))"
cur.execute(Command)