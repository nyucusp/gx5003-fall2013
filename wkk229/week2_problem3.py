#main idea is you want the ration of number of incidents /population for each borough
import csv

from _collections import defaultdict
#calculate number of accidents / create dictionaries fo ach file
#end product is:each line the name of borough and the calculated ratio 
#the lines should be sorted by alphabetically 

#creating dictionaries for each file 
#number of incidents per borough
#first open all files
zip=csv.reader(open('zipCodes.csv','rb'),delimiter=',')
zipcodePopDict=defaultdict(list)

for line in zip:
	zipcodePopDict.append(population)
	zipcodePopDict=dict((zipcode,tuple(line for zipcode,population in zipcodePopDict.iteritems())))
	print line

zipcodeIncidentsDict(zipcode,incedents)
incedent =csv.reader(open("incedents.csv",'rb'),delimiter=',')
for line in incedents:
	zipcode = perse(line)  #pass the zipcode and get line
if zipcodeIncidenstDict.keys(zipcode):

 #you get the number the dictionary and the keys contain zipcode
 #if the zip code is already there add 1
 	zipcodeIncidenstDict(zipcode).value +=1
else:
 	zipcodeIncidenstDict.append(zipcode,1)
#if that zipcode is not in the dictionary then add it (Append)


 #module3

 #use the zipcode to connect the three files-since each zipcode is common
 #find which zipcode of what you find are in the dictionary
 	boroughDict (borough,zipcodes) #loopsthrough the borough and dict
 	output =boroughDict (borough,n)
for borough in boroughDict.keys ():
 	population=(0)
 	incidents=(0)
for zipcode in boroughDict (borough):
 	population += zipcodePopDict(zipcode)
 	incidents += zipcodeIncidenstDict(zipcode)

 	#for each borough you need to have one unique n
 	n= incidents/population
 	output.append(borough,n)
 	print n



	
