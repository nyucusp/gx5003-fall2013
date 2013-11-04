import MySQLdb
import sys

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="jj1006", # your username
                     passwd="jpwd", # your password
                     db="coursedb") # name of the data base
# The Cursor object will let you execute the sql commands
cur = db.cursor()
cur.execute("select population/area from zipCodes where zip='"+sys.argv[1]+"';")
print cur.fetchall()[0][0]
db.close()
