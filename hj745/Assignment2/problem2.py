import csv
from collections import defaultdict
import re

data = defaultdict(list) # this is a dictionary whose value defaults to a list

for i, row in enumerate(csv.reader(open('zipCodes.csv', 'rb'))): #open the zipCodes.csv file and iterate over every row in it.
                                                                #Also, I can get incrementing row number by 'enumerate'
    if not i or not row: #set the first row indexed at i=0 as false so that I can skip the header line and any empty rows
        continue
    #set the all of columns in the cvs file into local variables
    name, zip_code_tabulation_area, zt36_d00, perimeter, lsad_trans, zt36_d00_i, lsad, area, latitude, longitude, Total_Population_per_ZIP_Code = row
    
    data[name].append(float(Total_Population_per_ZIP_Code)) # append the population numbers which are in 'Total_Population_per_ZIP_Code' column
                                                            # for each zipcode data, which are in 'name' column.
outputFile = open('output_density_problem2.txt','w') # open the output file

for name, Total_Population_per_ZIP_Code in data.iteritems(): # iterate over each zipcode and its population
    density = sum(Total_Population_per_ZIP_Code)/float(area) # calculate sum of population and population density, and set it as 'density' 
    out = name + " " + str(density) # set the two output of 'name' and 'density' into one argument. To do it, I converted 'density' to string)
    outputFile.write(out) # write 'out' on the output file
outputFile.close()
