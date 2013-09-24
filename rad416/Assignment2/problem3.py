
from _collections import defaultdict

incidentFile = open('Incidents_grouped_by_Address_and_Zip.csv','r')
next(incidentFile) #skip header row
incidentSplit = [] #list for file elements
for line in incidentFile:
  lineSplit = line.split(",")
  if(len(lineSplit[1]) >= 5):
    incidentSplit.append(lineSplit[1][ :5])
  
#close file
incidentFile.close()


zipDict = defaultdict(int)

for k in incidentSplit:
  zipDict[k] += 1

# print sorted(zipDict)



