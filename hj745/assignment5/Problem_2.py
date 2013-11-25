import csv
import MySQLdb
import matplotlib.pyplot as plt
import pandas as pd

    #To count all timestamp of submission per day, 'Group By' SQL query is one of easiest way to make the result so that I decided to use SQL as follows 
    #connect to database
db = MySQLdb.connect(host="localhost", user="hj745", passwd="000000", db="coursedb")
 
    #The Cursor object executes the sql commands
cur = db.cursor()  
 
    #create Timestamp table with DATETIME attributes in the actions-fall-2007.dat file
createTimestamp = "create table Timestamp (timestamp DATETIME)"
cur.execute(createTimestamp)

    #import data from actions-fall-2007.dat file to Timestamp table
queryTimestamp = "LOAD DATA LOCAL INFILE 'actions-fall-2007.dat' INTO TABLE Timestamp Lines terminated by '\n' IGNORE 1 LINES " 
cur.execute(queryTimestamp)

    #commit the changes before closing connection. Else the data would not be inserted.
db.commit()

    #I make the histogram with a bin of one day because it would be the most proper way to find submit pattern with regard to assignment due
    #So, I count all timestamp in one day by using 'Group By'
cur.execute("SELECT date(timestamp) from timestamp group by date(timestamp)")
    #result of SELECT COUNT contains a tuple with one element, so it should be come in with the number of rows only
result_x = [item[0] for item in cur.fetchall()]
    #count all timestamps in each day
cur.execute("SELECT COUNT(*) from timestamp group by date(timestamp)")

    #result of SELECT COUNT contains a tuple with one element, so it should be come in with the number of rows only
result_y = [item[0] for item in cur.fetchall()]

    #process the result in the bar histogram
plt.bar(result_x, result_y, width=1, align='center', color='green')

    
plt.show()

    #close connection
db.close()
    


