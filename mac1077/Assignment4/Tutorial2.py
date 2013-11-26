import MySQLdb
   
db = MySQLdb.connect(host="localhost", user="mac1077", passwd="miquel", db="coursedb") 
 
cur = db.cursor()  
 
createCommand = "create table test (id int not null, name varchar(255), age int, primary key(id))"
cur.execute(createCommand)

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