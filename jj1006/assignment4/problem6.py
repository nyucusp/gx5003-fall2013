import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="jj1006", # your username
                     passwd="jpwd", # your password
                     db="coursedb") # name of the data base
# The Cursor object will let you execute the sql commands
cur = db.cursor()
cur.execute("select z.zip,z.population from boroughs b, incidents i, zipCodes z where b.borough=\"Manhattan\" and b.zip=i.zip and i.zip=z.zip;")
print cur.fetchall()
db.close()
