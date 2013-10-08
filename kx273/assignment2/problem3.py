import csv  #read the csv file

popFileRaw = open('zipCodes.csv','r') #open the population file
popFile=csv.DictReader(popFileRaw, delimiter=',')

zipDict={} # define a dictionary for zip

for line in popFile:# input the population info to zipDict
   if (line['Total Population per ZIP Code']!=''):
      pop=int(line['Total Population per ZIP Code'])
      zipcode=str(line['zip code tabulation area'])
      zipDict[zipcode]={'population':pop,'incident':0,'borough':''}
popFileRaw.close()
      
incidentFileRaw = open('Incidents_grouped_by_Address_and_Zip.csv','r') #open incidenrt file
incidentFile=csv.DictReader(incidentFileRaw, delimiter=',')

for line in incidentFile: #input the number of incidents to zipDict
   zipcode=str(line['Incident Zip'])
   if zipcode in zipDict:
      zipDict[zipcode]['incident']+=1
incidentFileRaw.close()

boroFileRaw = open('boroughs.csv','r') # open borough file
boroFile=csv.reader(boroFileRaw, delimiter=',')

boroDict={} #define a dictionary for incident ratio of boroughs
for line in boroFile: # input the borough info to zipDict
   zipcode=str(line[0])
   if zipcode in zipDict:
      zipDict[zipcode]['borough']=line[1]
   if line[1]!='':
      boroDict[line[1]]={'population':0,'incident':0,'incidentratio':0}
boroFileRaw.close()

for zipcode in zipDict: # calculate the cumulative incident and population
   boro= zipDict[zipcode]['borough']
   if boro in boroDict:
      boroDict[boro]['population']+=int(zipDict[zipcode]['population'])
      boroDict[boro]['incident']+=int(zipDict[zipcode]['incident'])

outputFile = open('output_problem3.txt','w')
outputFile.write("Borough"+" "+"IncidentRatio"+"\n")
for boro in boroDict: #calculate the incident ratio
   boroDict[boro]['incidentratio']= round(float(boroDict[boro]['incident'])/float( boroDict[boro]['population']),4)
   lineFormat =boro + " " + str(boroDict[boro]['incidentratio']) + "\n" #convert dictionary to string for output  
   outputFile.write(lineFormat)
outputFile.close()
