import MySQLdb

#connect to database
db = MySQLdb.connect(host="localhost", # your host
                     user="cbj238", # your username
                     passwd="1nuU69y0",
                     db="coursedb")

# The Cursor object will let you execute the sql commands
cur = db.cursor()

# create a table with these three attributes
createCommand = "create table test (id int not null, name varchar(255), ge int, primary key(id))"
cur.execute(createCommand)
# Now we will insert 10 rows into this table
for i in range(10):
    name = "name" + str(i)
    age = 20 + i
    # create command to insert this into the table
    insertCommand = "insert into test values({0}, '{1}', {2});".format(i, name, age)
    cur.execute(insertCommand)

# You must commit the changes before closing connection. Else the data would not be inserted
db.commit()
# close connection
db.close()

