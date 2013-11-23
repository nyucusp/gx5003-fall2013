import MySQLdb
import csv
   
 #connect to database
db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="courseuser", # your username
                       passwd="password", # your password
                       db="coursedb") # name of the data base
 
 #The Cursor object 
cur = db.cursor()  

 #Delect tables if they exist 
try:
    cur.execute('DROP TABLE incidents')
    cur.execute('DROP TABLE zipcodes')
    cur.execute('DROP TABLE boroughs')
except:
    pass

 #define function: if the input is int, return the string of int number, otherwise return the string of NULL
def intcheck(string):
    try:
        intnum=int(string)
        return str(intnum)
    except:
        return "NULL"

 #define function: if the input is float, return the string of float number, otherwise return the string of NULL
def floatcheck(string):
    try:
        floatnum=float(string)
        return str(floatnum)
    except:
        return "NULL"


 # crete a table with three attributes
createCommand = "create table boroughs (id int not null,zipcode char(50), borough char(50), primary key(id))"
cur.execute(createCommand)

createCommand = "create table zipcodes (id int not null,name char(50), zip_code_tabulation_area char(50),zt36_d00 int, perimeter float,lsad_trans char(50),zt36_d00_i int,lsad char(10),area float, latitude float, longitude float, total_population_per_zip_code int, primary key(id))"
cur.execute(createCommand)

createCommand = "create table incidents (id int not null,incident_address varchar(255), incident_zip char(50),unique_key int,  primary key(id))"
cur.execute(createCommand)

 
#Now read the csv files and insert it into the database
boroFileRaw = open('boroughs.csv','r') # open borough file
boroFile=csv.reader(boroFileRaw, delimiter=',')
i=1
for line in boroFile:
    try:
        insertCommand= "insert into boroughs values(" + str(i) + ","+"'"+str(line[0])+"'"+","+"'"+str(line[1])+"'" + ")"
        cur.execute(insertCommand)
    except:
        pass
    i+=1
boroFileRaw.close()

zipFileRaw = open('zipCodes.csv','r') # open zipCodes file
zipFile=csv.DictReader(zipFileRaw, delimiter=',')
i=1
for line in zipFile: 
    try:
        insertCommand= "insert into zipcodes values(" + str(i) + ","+"'"+str(line['name'])+"'" + ","+"'"+str(line['zip code tabulation area'])+"'" + ","+intcheck(line['zt36 d00'])+ ","+floatcheck(line['perimeter']) + ","+"'"+str(line['lsad trans'])+"'" + ","+intcheck(line['zt36 d00 i']) + ","+"'"+str(line['lsad'])+"'" + ","+floatcheck(line['area'])+ ","+floatcheck(line['latitude']) + ","+floatcheck(line['longitude']) + ","+intcheck(line['Total Population per ZIP Code']) + ")"
        cur.execute(insertCommand)
    except:
        pass
    i+=1
zipFileRaw.close()

incFileRaw = open('Incidents_grouped_by_Address_and_Zip.csv','r') # open incident file
incFile=csv.DictReader(incFileRaw, delimiter=',')
i=1
for line in incFile: 
    try:
        insertCommand = "insert into incidents values(" + str(i)+  ","+'"'+str(line['Incident Address'].strip())+'"'+  ","+'"'+str(line['Incident Zip'])+'"'+","+intcheck(line['Unique Key']) + ")"
        cur.execute(insertCommand)
    except:
        pass
    i+=1
incFileRaw.close()

 # commit the changes before closing connection. 
db.commit()	
 #close connection
db.close()
