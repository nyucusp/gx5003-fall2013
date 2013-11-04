import MySQLdb
   
# First we connect to the database
db = MySQLdb.connect(host="localhost", 
                      user="rs4606", 
                       passwd="a1s2d3f4", 
                       db="coursedb") 

 
# Next we create a cursor object
cur = db.cursor()  
 
# Create the boroughs table with two attributes
createCommand = "create table if not exists boroughs (zip varchar(255), borough_name varchar(255))"
cur.execute(createCommand)
 
# Create the zipcodes table with three attributes
createCommand2 = "create table if not exists zipcodes (zip varchar(255), area decimal(10,9), population decimal)" 
cur.execute(createCommand2)
 
# Create the incidents table with two attributes
createCommand3 = "create table if not exists incidents (zip varchar(255), address varchar(500), incident_count int)"
cur.execute(createCommand3)



"""
Inserting data into the boroughs file.  Further information is in the report.txt file
"""



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

# Here we remove duplicates from the boroughs file
removeduplicates = "ALTER IGNORE TABLE boroughs ADD UNIQUE INDEX (zip)"
cur.execute(removeduplicates)




 
"""
Inserting data into the zipcodes table.  Further information is in the report.txt file
"""
 
zipcodes_file = open('zipCodes.csv', 'r')

lines = []
for line in zipcodes_file:
    lines.append(line)
zipcodes_file.close()


# Here we make a dict which takes the last occurrence in the file of each zip code 
zip_dict = {}
for i in range(1, len(lines)):
    if lines[i].split(',')[10] != "\n":
        zip_dict[lines[i].split(',')[0]] = (float(lines[i].split(',')[10]), float(lines[i].split(',')[7]))


# Here we insert the keys and values from the dict into the zipcodes table
for key in zip_dict:
    insertCommand2 = "insert into zipcodes values(" + "'" + key + "'" + "," + str(zip_dict[key][1]) + "," + str(zip_dict[key][0]) + ");"
    cur.execute(insertCommand2)
 




"""
Inserting data into the incidents table.  Further information is in the report.txt file
"""
incident_file = open('incidents.csv', 'r')

incident_lines = []
for line in incident_file:
    incident_lines.append(line)
incident_file.close()

zip_incident_list = []
num_incident_lines = len(incident_lines)

for i in range(1, num_incident_lines):
    zip_incident_list.append(incident_lines[i].split(',')[1]) 

"""
Here we insert the zipcode (first five digits of numeric zip codes; 
other bad data is excluded.  We insert the incident address next, but we have to remove 
apostrophes to properly insert the data into the database.  Finally, we insert the
integer count of the number of incidents at that address.
"""
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