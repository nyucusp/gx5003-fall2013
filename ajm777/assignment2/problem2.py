#Aliya Merali
#Assignment 2
#Problem 2

import csv
zipfile = open('zipCodes.csv','r')
outputFile = open('output_density_problem2.txt','w')

zipDict = csv.DictReader(zipfile) #Using the csv module to read in the file as a dictionary
outputData  = {} #Creating an empty dictionary for the output
for row in zipDict: #filtering through the data dictionary
    if row['Total Population per ZIP Code'] != '': #if there is a value for population, then:
        pop = row['Total Population per ZIP Code']
        area = row['area']
        density = int(pop)/float(area)
        zipcode = row['name']
        outputData[zipcode] = density #populating the output dictionary
        sortedData = outputData.items() #sorting output dict
        sortedData.sort()
        for z, d in sortedData:
            writeData = str(z) + ' ' + str(d) + "\n" #Creating a string value to output to the txt file

        outputFile.write(writeData)

outputFile.close()
