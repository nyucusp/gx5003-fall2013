#Aliya Merali
#Urban Informatics
#Assignment 4
#Problem 1 - create 3 tables & populate from csv files

import csv
import MySQLdb
import re

zip_data_file = open('zipCodes.csv','r')
bor_data_file = open('boroughs.csv','r')
inc_data_file = open('Incidents_grouped_by_Address_and_Zip.csv','r')

#connect to database
db = MySQLdb.connect(host="localhost",user="ajm777",passwd="pepper89",db="coursedb")
cur = db.cursor()  

#_______________CREATING DATABASES_________________
create_zip = "create table zip_code (zip_code varchar(10), area float not null, pop_by_zip int)"
create_bor = "create table bor (zip_code varchar(10) not null, name text not null)"
create_inc = "create table inc (address varchar(500), zip_code varchar(10) not null, num_inc int)"

#Stop the warnings from appearing from the drop if exists commmand
import warnings
warnings.filterwarnings("ignore", "Unknown table.*")
#So I can create the table over again when needed, use the drop if exists command
cur.execute('DROP TABLE IF EXISTS create_zip')
cur.execute('DROP TABLE IF EXISTS create_bor')
cur.execute('DROP TABLE IF EXISTS create_inc')

#____________________FILLING DATABASES_________________
#Getting the zip code data in a format to be put into the table
zip_data_read = csv.DictReader(zip_data_file)
for line in zip_data_read: 
    zip_val = line['name']
    area = line['area']
    pop_by_zip = str(line['Total Population per ZIP Code'])
    zip_val_list =  list(zip_val)
    if zip_val_list[3] != 'H' and pop_by_zip != ' ' and pop_by_zip != '': #ignores dirty data with HH zipcode or emptly pop value
        insert_command = "insert into zip_code values(" + "'" + zip_val + "'" + "," + "'" + area + "'" + "," + "'" + pop_by_zip + "'"  ");"
        cur.execute(insert_command)
#print "Zip Table Filled!"

#Getting borough data in format to be put into the table & Filling the bor table
bor_data_read = csv.reader(bor_data_file)
for line in bor_data_read:
    zip_val = str(line[0])
    bor_name = str(line[1])
    insert_command = "insert into bor values(" + "'" + zip_val + "'" + "," + "'" + bor_name + "'" ");"
    cur.execute(insert_command)
#print "Borough Table Filled!"

#Getting incident data in format for inupt & filling the inc table
inc_data_read = csv.DictReader(inc_data_file)
for line in inc_data_read: 
    address = line['Incident Address']
    zip_val_whole = line['Incident Zip']
    zip_val = re.findall(r'\d+',zip_val_whole)
    zip_val = list(zip_val)[:5] #getting just the first 5 digits of the zip-code
    zip_val = ''.join(zip_val)
    inc_count = str(line['Unique Key'])
    if "'" in list(address): #To solve issue of ' in st. like St. John's
        address = address.replace("'","")
    if zip_val != '':
        insert_command = "insert into inc values(" + "'" + str(address) + "'" + "," + "'" + zip_val + "'" + "," + "'" + inc_count + "'"  ");"
        cur.execute(insert_command)
#print "Incident Table Filled!"

db.commit()	
db.close()
