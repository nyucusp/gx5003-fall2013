import MySQLdb
   
 #connect to database
 db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 # The Cursor object will let you execute the sql commands
 cur = db.cursor()  
 
 # crete a table with three attributes
 createCommand = "create table test (id int not null, name varchar(255), age int, primary key(id))"
 cur.execute(createCommand)
 #Now we will insert 10 rows into this table
 for i in range(10):
  name = "name" + str(i)
  age = 20 + i
  # create command to insesrt this into the table
  insertCommand = "insert into test values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
  cur.execute(insertCommand)
 
 
 # You must commit the changes before closing connection. Else the data would not be inserted.
 db.commit()    
 # close connection
 db.close()