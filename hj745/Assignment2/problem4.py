import sys
import csv
from collections import defaultdict
import re

borough_in = sys.argv[1] #receive input of "09/19/2013 09:12:15" in the command

class Borough: #this is the class of Borough from tutorial 2
   name = None
   zipcodes = None

   def __init__(self, name):
      self.name = name
      zipcodes = []
      
   def addZipcode(self, zip):
      zipcodes.append(zip)
      
data = defaultdict(list) # this is a dictionary whose value defaults to a list

for i, row in enumerate(csv.reader(open('zipCodes.csv', 'rb'))): #open the zipCodes.csv file and iterate over every row in it.
                                                                #Also, I can get incrementing row number by 'enumerate'
    if not i or not row: #set the first row indexed at i=0 as false so that I can skip the header line and any empty rows
        continue
    #set the all of columns in the zipCodes.cvs file into local variables
    name, zip_code_tabulation_area, zt36_d00, perimeter, lsad_trans, zt36_d00_i, lsad, area, latitude, longitude, Total_Population_per_ZIP_Code = row
    
    data[name].append(float(Total_Population_per_ZIP_Code)) # append the population numbers which are in 'Total_Population_per_ZIP_Code' column
                                                            # for each zipcode data, which are in 'name' column.
outputFile = open('output_problem3_2.csv','w') # open the output file

for name, Total_Population_per_ZIP_Code in data.iteritems(): # iterate over each zipcode and its population
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
