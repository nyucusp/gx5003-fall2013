import MySQLdb

db = MySQLdb.connect(host="localhost", user="jsa325", passwd="M1nd=B0dy", db="coursedb")
 
cur = db.cursor()  
 
createCommand = "create table test (id int not null, name varchar(255), age int, primary key(id))"
cur.execute(createCommand)
for i in range(10):
 	name = "name" + str(i)
 	age = 20 + i
 	insertCommand = "insert into test values(" + str(i) + "," + "'" + name + "'" + "," + str(age) + ");"
 	cur.execute(insertCommand)
 
 
db.commit()	
db.close()
