# zipIncidentDict [zipcode -> incidents]
# boroughZipDict [borough -> [zipcode1, zipcode2,...,zipcodeN]]
# boroughPopDict [borough -> population]
# boroughIncidentDict [borough -> incidents]
# zipPopDict [zipcode -> population]


# files are processed from a file to a list of elements and finally
# into a dictionary for aggregation purposes because there are 
# multiple entries for zip code populations and other effects to 
# manage with the data

from subprocess import call
from _collections import defaultdict

########################################
# Create Borough -> Zip relation       #
########################################

#fix formatting in boroughs file prior to load
call("tr '\r' '\n' < boroughs.csv > boroughs_tr2.csv", shell=True)

#load fixed file
boroughZipFile = open('boroughs_tr2.csv','r')

boroughZipList = [] #list to contain the file elements

#populate boroughZipList
for line in boroughZipFile:
  lineSplit = line.split(",")
  boroughZipList.append([lineSplit[0], lineSplit[1].rstrip()])

boroughZipFile.close() #close boroughs_tr.csv file

boroughZipDict = defaultdict(list) #dict to organize zipcodes into boroughs

#populate dict with elements from list keyed on borough
for v,k in boroughZipList:
  boroughZipDict[k].append(v)

####################################
# Create Zip -> Incidents relation #
####################################
#fix formatting in Incidents file prior to load
call("tr '\r' '\n' < Incidents_grouped_by_Address_and_Zip.csv > Incidents_grouped_by_Address_and_Zip_tr2.csv", shell=True)

zipIncidentFile = open('Incidents_grouped_by_Address_and_Zip_tr2.csv','r')
next(zipIncidentFile) #skip header row
zipIncidentList = [] #list for file elements
for line in zipIncidentFile:
  lineSplit = line.split(",")
  if(len(lineSplit[1]) >= 5):
    zipIncidentList.append([lineSplit[1][ :5],int(lineSplit[2].rstrip())])

#List in format [zipcode, incidents (#)] (non-aggregate)
  
#close file
zipIncidentFile.close()

zipIncidentDict = defaultdict(int) #dict to capture zipcodes and counts

#aggregate by zipcode in dict
for i in range(len(zipIncidentList)):
    zipIncidentDict[zipIncidentList[i][0]] += zipIncidentList[i][1]

########################################
# Create Borough -> Incident relation  #
########################################

boroughIncidentDict = defaultdict(int)

#iterate through boroughs and aggregate incidents from zipIncidentDict
for k in boroughZipDict:
  incidentSum = 0
  for v in boroughZipDict[k]:
    incidentSum += zipIncidentDict[v]
  boroughIncidentDict[k] = incidentSum

########################################
# Create Zip -> Population relation    #
########################################

#create population by zip code
zipPopFile = open('zipCodes.csv','r')
next(zipPopFile) #skip header row

zipPopList = [] #list for file contents

#populate zipList
for line in zipPopFile: 
  lineSplit = line.split(",")
  if(lineSplit[10] != '\n'): #skip if population is empty
    zipPopList.append([lineSplit[1],lineSplit[10].rstrip()])

zipPopFile.close() #close file

zipPopDict = defaultdict(list) #dict to capture population in zipcode

#convert list to dict
for k,v in zipPopList:
  zipPopDict[k].append(v)

#combine multiple population figures for zipcodes with multiple pop entries
for k in zipPopDict:
  if(len(zipPopDict[k])>1):
    zipPopDict[k] = [str(int(zipPopDict[k][0]) + int(zipPopDict[k][1]))]

#########################################
# Create Borough -> Population relation #
#########################################

boroughPopDict = defaultdict(int)
#iterate through boroughs and aggregate population from zipPopDict
for k in boroughZipDict:
  population = 0
  for v in boroughZipDict[k]:
    if zipPopDict[v]: #test for not null
      population += int(zipPopDict[v][0])
  boroughPopDict[k] = population

##################################################
# Create Borough -> Incidents:Pop ratio relation #
##################################################

boroughRatioDict = defaultdict(float)

#generate borough incidents per person ratio as dictionary value
for k in boroughIncidentDict:
  boroughRatioDict[k] = float(boroughIncidentDict[k])/float(boroughPopDict[k])

##################################################
# Output Borough -> Incidents:Pop ratio relation #
##################################################

outFile = open('output_problem3.txt','w')
outFile.write("Incidents per capita for each NYC borough\n")
for k in sorted(boroughRatioDict):
  outFile.write(k)
  outFile.write(" ")
  outFile.write(str(boroughRatioDict[k]))
  outFile.write('\n')

outFile.close()