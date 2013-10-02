# Compute the average population of the zip codes in a given borough
import sys

from zipcode import Zipcode
from borough import Borough

targetBorough = Borough(sys.argv[1].split(" ")[0])

fileBorough = open('boroughs_tr.csv','r')
linesBorough = []

for line in fileBorough:
  linesBorough.append(line)
fileBorough.close()

zipBoroughDict = {}  # create dictionary as in problem3.py
num_linesBorough = len(linesBorough)

for i in range(1, num_linesBorough):
  if linesBorough[i].split(',')[10] != '\n':
    zipBoroughDict[linesBorough[i].split(',')[0] = (float(linesBorough[i].split(',')[1][:-1]))

filePopulation = open('zipCodes_tr.csv', 'r')
linesPopulation = []

for line in filePopulation:
  linesPopulation.append(line)
filePopulation.close()

zipPopulationDict = {}  # create dictionary as in problem3.py
num_linesPopulation = len(linesPopulation)

for i in range(1, num_linesPopulation):
  if linesPopulation[i].split(',')[10] != '\n':
    zipPopulationDict[linesPopulation[i].split(',')[0] = (float(linesPopulation[i].split(',')[10]))

# Last part
    
for zip in zipBoroughDict:
    if zipBoroughDict[zip][0:5] == targetBorough[0:5]:
        if zip in zipPopulationDict: 
            zipCode = zipcode.Zipcode(zip, zipPopulationDict[zip])
            targetBorough.addZipcode(zipCode)

# Output average population

average = targetBorough.averagePopulation()
print average
