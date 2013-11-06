import csv
from collections import defaultdict
import re


f1 = file('boroughs.csv', 'r') #open boroughs.csv
f2 = file('Incidents_grouped_by_Address_and_Zip.csv', 'r') # open Incidents_grouped_by_Address_and_Zip.csv
f3 = file('results.csv', 'w')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

#Code for calculating the number of incidents for each borough -BEGIN

IncidentList = [row for row in c2] # set the zipcodes that contain incidents

for Borough_row in c1:
    row = 0
    found = False
    for Incident_row in IncidentList: 
        Results_row = Borough_row 
        if Borough_row[0] == Incident_row[1]: # check if the zipcode in boroughs.csv is the same as that in Incidents_grouped_by_Address_and_Zip.csv'
            Results_row.append('1') #if zipcodes, which are in Incidents_grouped_by_Address_and_Zip.csv file, are found in boroughs.csv file, then print '1' in the Results.csv file
                                    # this is to compute the number of incidents for each borough by iterating over every row for each Borough
            found = True
            break
        row = row + 1
    if not found:
        Results_row.append('0') #if zipcodes, which are in Incidents_grouped_by_Address_and_Zip.csv file, are NOT found in boroughs.csv file, then print '0' in the Results.csv file
                                    # this is to compute the number of incidents for each borough by iterating over every row for each Borough
    c3.writerow(Results_row)

data1 = defaultdict(list) # this is a dictionary whose value defaults to a list

for i, row in enumerate(csv.reader(open('Results.csv', 'rb'))): #open the Results.csv file and iterate over every row in it.
                                                                #Also, I can get incrementing row number by 'enumerate'
    if not i or not row: #set the first row indexed at i=0 as false so that I can skip the header line and any empty rows
        continue
    #set the all of columns in the Results.cvs file into local variables
    Zip, Boroughs, 0  = row # Zip, Boroughs, 0, these 3 are the column name in the Results.csv file
    
    data1[Boroughs].append(float(0)) # append the number of incident which are in '0' column
                                    # for each Borough data, which are in 'Boroughs' column.
outputFile = open('output_problem3_1.txt','w') # open the output file

for Boroughs, 0 in data1.iteritems(): # iterate over each borough and its umber of incident
    NumIncident = sum(0) # calculate the total number of incident  
    out = Boroughs + " " + str(NumIncident) # set the two output of 'Boroughs' and 'o' into one argument. To do it, I converted '0' to string
    outputFile.write(out) # write 'out' on the output file
outputFile.close()

#Code for calculating the number of incidents for each borough -END

#Code for calculating the number of population for each borough -BEGIN
data2 = defaultdict(list) # this is a dictionary whose value defaults to a list

for i, row in enumerate(csv.reader(open('zipCodes.csv', 'rb'))): #open the zipCodes.csv file and iterate over every row in it.
                                                                #Also, I can get incrementing row number by 'enumerate'
    if not i or not row: #set the first row indexed at i=0 as false so that I can skip the header line and any empty rows
        continue
    #set the all of columns in the zipCodes.cvs file into local variables
    name, zip_code_tabulation_area, zt36_d00, perimeter, lsad_trans, zt36_d00_i, lsad, area, latitude, longitude, Total_Population_per_ZIP_Code = row
    
    data2[name].append(float(Total_Population_per_ZIP_Code)) # append the population numbers which are in 'Total_Population_per_ZIP_Code' column
                                                            # for each zipcode data, which are in 'name' column.
outputFile = open('output_problem3_2.csv','w') # open the output file

for name, Total_Population_per_ZIP_Code in data2.iteritems(): # iterate over each zipcode and its population
    if (Total_Population_per_ZIP_Code > 10000) and (Total_Population_per_ZIP_Code < 10283): # set the range of zipcode for Manhattan
        name = 'Manhattan'
    elif (Total_Population_per_ZIP_Code > 10300) and (Total_Population_per_ZIP_Code < 10315): # set the range of zipcode for Staten
        name = 'Staten'
    elif (Total_Population_per_ZIP_Code > 10450) and (Total_Population_per_ZIP_Code < 10476): # set the range of zipcode for Bronx
        name = 'Bronx'
    elif (Total_Population_per_ZIP_Code > 11003) and (Total_Population_per_ZIP_Code < 11698):# set the range of zipcode for Queens
        name = 'Queens'
    elif (Total_Population_per_ZIP_Code > 11200) and (Total_Population_per_ZIP_Code < 11257):# set the range of zipcode for Brooklyn
        name = 'Brooklyn'

    Population = sum(Total_Population_per_ZIP_Code) # calculate sum of population 
    out = name + "," + str(Population) # set the two output of 'name' and 'population' into one argument. To do it, I converted 'Population' to string
                                       # Also, in order to caculate the population for each borough, it would be better for this output to be recorded in the csv file
                                       # so, inserted ',' to seperate into 2 column
    outputFile.write(out) # write 'out' on the output file
outputFile.close()

# To calculate the population for each borough, I call the output_problem3_2.csv file, which contains the population for borough per rows as below

data3 = defaultdict(list) # this is a dictionary whose value defaults to a list

for i, row in enumerate(csv.reader(open('output_problem3_2.csv', 'rb'))): #open the output_problem3_2.csv file and iterate over every row in it.
                                                                        #Also, I can get incrementing row number by 'enumerate'
    if not i or not row: #set the first row indexed at i=0 as false so that I can skip the header line and any empty rows
        continue
    #set the all of columns in the output_problem3_2.csv file into local variables
    name,Total_Population_per_ZIP_Code = row
    
    data3[name].append(float(Total_Population_per_ZIP_Code)) # append the population numbers which are in 'Total_Population_per_ZIP_Code' column
                                                            # for each borough name data, which are in 'name' column.
outputFile = open('output_problem3_3.txt','w') # open the output file

for name, Total_Population_per_ZIP_Code in data3.iteritems(): # iterate over each borough name and its population
    
    Population = sum(Total_Population_per_ZIP_Code) # calculate sum of population for each borough name 
    out = name + " " + str(Population) # set the two output of 'name' and 'population' into one argument. To do it, I converted 'Population' to string)
    outputFile.write(out) # write 'out' on the output file
outputFile.close()
#Code for calculating the number of population for each borough -END

f1.close()
f2.close()
f3.close()

