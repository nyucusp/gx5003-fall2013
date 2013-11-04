import MySQLdb

user_input = raw_input("Enter borough name: ")

#I already know that the value of total_population_per_zip_code column is string, so that I convert the input value type to string
user_input2=str(user_input)

#connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
# The Cursor object executes the sql commands
cur = db.cursor()

# query total population per borough that is entered though the command line
#there are many duplicates in the boroughs.csv file, so I make the newBoroughs that contains only different values and use it for the left join to draw the number of total population per particular borough that is entered as an input in the command line 
#Also, there are some empty cells in total population column, so I select only cells that contain values without being leaved empty
cur.execute('select sum(total_population_per_zip_code) from zipcodes left join (select distinct zip, borough from boroughs) newBoroughs on zipcodes.name=newBoroughs.zip where newBoroughs.borough=%s and zipcodes.total_population_per_zip_code != ""',user_input2)
rows = cur.fetchall()
for row1 in rows:
    print row1[0]

# query total incidents per borough that is entered though the command line
#there are many duplicates in the boroughs.csv file, so I make the newBoroughs that contains only different values and use it for the left join to draw the number of total population per particular borough that is entered as an input in the command line 
#Also, there are some empty cells in total population column, so I select only cells that contain values without being leaved empty
#In order to calculate the total number of incidents, I add all of unique keys in Incidents table
cur.execute('select sum(unique_key) from incidents left join (select distinct zip, borough from boroughs) newBoroughs on incidents.incident_zip=newBoroughs.zip where newBoroughs.borough=%s',user_input2)
# process the result
rows = cur.fetchall()
for row2 in rows:
    print row2[0]

#compute the ratio between the number of incidents and the population in that borough
# I convert the data type of total number of population to integer because operand type is not supported for decimal or float
print row2[0]/int(row1[0])
 
# close connection
db.close()
