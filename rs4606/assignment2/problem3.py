import sys
from collections import Counter


"""
We first open zipCodes and save the lines as elements in a list called zip_lines.

Next, we create a dict and populate it with zipcodes as keys and populations
as values.  We ignore those zipcodes that have no population information 
with the "if" clause.  

Note that there are apparently duplicate zip codes in the zipCodes file 
(meaning duplicate zip codes with *different* population values).  Since I have no 
idea what the correct population is, for a given zip code I am just
putting the *last* instance of it (the last instance in the order it appears in the 
zipCodes.csv file) in the dictionary below.
"""
myFile = open('zipCodes.csv', 'r')

zip_lines = []
for line in myFile:
    zip_lines.append(line)
myFile.close()

zip_pop_dict = {}
num_zip_lines = len(zip_lines)

for i in range(1, num_zip_lines):
    if zip_lines[i].split(',')[10] != "\n":
        zip_pop_dict[zip_lines[i].split(',')[0]] = (float(zip_lines[i].split(',')[10]))


"""
Now we make another dict, zip_incident_dict, and populate it with zipcodes as keys
and incident counts as values.  We need to read from the incidents csv file to do this.  
We get the incident counts by using the Counter method from collections, imported at the 
beginnning of the file.
"""
incident_file = open('Incidents_grouped_by_Address_and_Zip.csv', 'r')

incident_lines = []
for line in incident_file:
    incident_lines.append(line)
incident_file.close()

zip_incident_list = []
num_incident_lines = len(incident_lines)

for i in range(1, num_incident_lines):
    zip_incident_list.append(incident_lines[i].split(',')[1]) 

zip_incident_dict = Counter(zip_incident_list)


"""
Now we make an intermediate dict, boroughs_zip_dict, and populate it with zipcodes as 
keys and boroughs as values.  We need to read from the boroughs_tr.csv file to do this.  
"""
boroughs_file = open('boroughs_tr.csv', 'r')

boroughs_lines = []
for line in boroughs_file:
    boroughs_lines.append(line)
boroughs_file.close()

boroughs_zip_dict = {}
num_boroughs_lines = len(boroughs_lines)

for i in range(0, num_boroughs_lines):
    boroughs_zip_dict[boroughs_lines[i].split(',')[0]] = boroughs_lines[i].split(',')[1][:-1]

"""
Next, we reverse boroughs_zip_dict to make boroughs_dict.  Note that we have to 
manually remove the (incorrect) key "State" from boroughs_dict and add its value
to the value of the (correct) key "Staten"
"""

boroughs_dict = {}
for k, v in boroughs_zip_dict.iteritems():
    boroughs_dict[v] = boroughs_dict.get(v, [])
    boroughs_dict[v].append(k)
del boroughs_dict['State']
boroughs_dict['Staten'].append('10314')

"""
Now make a dict with boroughs as keys and the two element list [population, incident count]
as values.  

Note that we have to be a bit careful because there are some zip codes 
from the boroughs_tr.csv file that do not appear in the zipCodes.csv file!  

Note also that there is a lot of "bad data" in the zip_incident_dict file, because keys 
are not only 5 digit zip codes, but also strings of letters (e.g. "NEWARK INTERNATIONAL AIRPORT)
and 9 digit zip codes.  We deal with this by truncating each zip code in zip_incident_dict
to the first 5 characters and then comparing them with our given zip from the boroughs_tr.csv
file.  This effectively ignores the zip codes which are strings of letters but keeps
the incident counts from zip codes which are 9 digits (by only considering the first
5 digits).
"""


boroughs_pop_inc_count = boroughs_dict
for key in boroughs_pop_inc_count:
    count_pop = 0
    count_inc = 0
    for zip in boroughs_pop_inc_count[key]:
        if zip_pop_dict.get(zip) != None:
            count_pop += zip_pop_dict[zip]
        for inc_key in zip_incident_dict:
            if inc_key[0:5] == zip:
                count_inc += zip_incident_dict[inc_key]
    boroughs_pop_inc_count[key] = [count_pop, count_inc]   


"""
Finally we output, sort, and calculate the ratio of incidents divided
by population at the same time
"""

outputFile = open('output_problem3.txt', 'w')
for key in sorted(boroughs_pop_inc_count.iterkeys()):
    outputFile.write("%s %s \n" % (key, (boroughs_pop_inc_count[key][1])/(boroughs_pop_inc_count[key][0])))
outputFile.close()


