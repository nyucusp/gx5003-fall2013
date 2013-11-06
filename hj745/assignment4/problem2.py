import MySQLdb

user_input = raw_input("Enter zipcode: ")

#I already know that the value of total_population_per_zip_code column is string, so that I convert the input value type to string
user_input2=str(user_input)

#connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
# The Cursor object executes the sql commands
cur = db.cursor()

# query total population of zipcode that is entered though the command line
cur.execute('select total_population_per_zip_code from zipcodes where name=%s', user_input2)

# process the result
rows = cur.fetchall()
for row in rows:
    print row[0]
    
# close connection
db.close()
