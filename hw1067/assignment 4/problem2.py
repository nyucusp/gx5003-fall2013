    ##########################
    #Assignment4 Problem2    #
    #Haozhe Wang             #
    ##########################
import sys
import MySQLdb


#zipinput = sys.argv[1]
zipinput = sys.argv[1]

db = MySQLdb.connect(host = 'localhost',
                     user = 'hw1067',
                     passwd = '81828384yomama',
                     db = 'coursedb')
cur = db.cursor()
                     
query = "select pop_by_zip/ area from zips where zip_code = "+ "'" + zipinput + "'" +";"
cur.execute(query)

#print cur.fetchall()

for row in cur.fetchall() :
    print row
# close connection
db.close()

