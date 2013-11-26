import MySQLdb
   
# Connection to DB
db = MySQLdb.connect(host="localhost", user="mac1077", passwd="miquel", db="coursedb") 
 
# Create Cursor Object
cur = db.cursor()  
 
# Creation of Borough Tables #1 (2 atributes)
createCommand = "CREATE TABLE IF NOT EXISTS borough (zip varchar(255), borough_name varchar(255))"
cur.execute(createCommand)
 
# Creation of Zipcode Tables #2 (2 atributes)
createCommand2 = "CREATE TABLE IF NOT EXISTS zipcodes (zip varchar(255), area decimal(10,9), population decimal)" 
cur.execute(createCommand2)
 
# Creation of Incidents Tables #3 (2 Atributes)
createCommand3 = "CREATE TABLE IF NOT EXISTS incidents (zip varchar(255), address varchar(500), incident_count int)"
cur.execute(createCommand3)


#Data inserted in bouroughs csv 


boroughs_file = open('boroughs.csv', 'r')

boroughs_lines = []
for line in boroughs_file:
    boroughs_lines.append(line)
boroughs_file.close()
 
for i in range(0, len(boroughs_lines)):
    borough_name = boroughs_lines[i].split(',')[1][:-1] 
    borough_zip_code = boroughs_lines[i].split(',')[0]
    insertCommand1 = "insert into boroughs values(" + "'" + borough_zip_code + "'" + "," + "'" + borough_name + "'" + ");"
    cur.execute(insertCommand1)

# duplicates are deleted in the bouroughs csv
removeduplicates = "ALTER IGNORE TABLE boroughs ADD UNIQUE INDEX (zip)"
cur.execute(removeduplicates)


#Data inserted in zipcodes csv
 
zipcodes_file = open('zipCodes.csv', 'r')

lines = []
for line in zipcodes_file:
    lines.append(line)
zipcodes_file.close()


#Dictionary created for zip codes
zip_dict = {}
for i in range(1, len(lines)):
    if lines[i].split(',')[10] != "\n":
        zip_dict[lines[i].split(',')[0]] = (float(lines[i].split(',')[10]), float(lines[i].split(',')[7]))


#Keys and values for Zipcode table
for key in zip_dict:
    insertCommand2 = "insert into zipcodes values(" + "'" + key + "'" + "," + str(zip_dict[key][1]) + "," + str(zip_dict[key][0]) + ");"
    cur.execute(insertCommand2)
 

#Data inserted in incidents csv

incident_file = open('incidents.csv', 'r')

incident_lines = []
for line in incident_file:
    incident_lines.append(line)
incident_file.close()

zip_incident_list = []
num_incident_lines = len(incident_lines)

for i in range(1, num_incident_lines):
    zip_incident_list.append(incident_lines[i].split(',')[1]) 


#Zipcodes inserted, only first 5 digits followed by the incident address formated. Then the number of incidents of the addres

for i in range(1, len(incident_lines)):
    incident_zip_code = incident_lines[i].split(',')[1][0:5]
    if (incident_zip_code.isdigit()):
        incident_address = incident_lines[i].split(',')[0].replace("'","")
        incident_count = incident_lines[i].split(',')[2][:-1]
        if incident_count.isdigit():
            insertCommand3 = "insert into incidents values(" + "'" + incident_zip_code + "'" + "," + "'" + incident_address + "'" + "," + "'" + incident_count + "'" + ");"
            cur.execute(insertCommand3)
 


db.commit()        
db.close()