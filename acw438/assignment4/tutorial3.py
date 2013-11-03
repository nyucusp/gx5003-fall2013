import MySQLdb

#connect to database
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')

#create cursor
cur = db.cursor()

#query all rows where age < 25:
query = 'SELECT * FROM test WHERE age < 25'
cur.execute(query)

#print out result:
for row in cur.fetchall():
    print str(row[0]), row[1], str(row[2])

#close connection
db.close()
