import MySQLdb

#connect to database
db = MySQLdb.connect(host='localhost', \
                     user='acw438', \
                     passwd='cusp', \
                     db='coursedb')

#create cursor object to execute sql commands
cur = db.cursor()

#create a table with three attributes:
#createCommand = "create table test (id int not null, name varchar(255), age int, primary key(id))"
#cur.execute(createCommand)

#Now insert 10 rows into the table
for i in range(10):
    name = "name " + str(i)
    age = 20 + i
    
    #create command to insert this into the table:
    insertCommand = "insert into test values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
    cur.execute(insertCommand)

#You must commit the changes before closing the connection.
#Otherwise, the data will not be inserted.
db.commit()
#Close connection:
db.close()
