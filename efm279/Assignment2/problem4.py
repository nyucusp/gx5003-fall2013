import sys
import csv
from zipcode import Zipcode
from borough import Borough

#get user input
userboro = sys.argv[1]


#read csv files
boro=csv.reader(open("boroughs.csv","rb"),delimiter=',')
b1=list(boro)
zips=csv.reader(open("zipCodes.csv","rb"),delimiter=',')
z3=list(zips)

#dictionary holding all zip codes' population from zipcodes.csv
zippop={}
#dictionary for borough, takes user input
boroughs={userboro:0}

#fill in zipcode
for i in range(1,len(z3)):
	zippop[z3[i][0]]=z3[i][10]

# instantiate Borough class in the dictionary
# class has 3 parameters, name, zipcodes as an array and sum of population in zip codes in the borough 
boroughs[userboro]=Borough(userboro)
boroughs[userboro].zipcodes=[]
boroughs[userboro].sumpopul=0

#first check if in boroughs.csv zip exists
#if we find user defined borough name proceed to zip population dictionary
#append the zip code to the class object
#zort is a list as (zipcode, population in the zipcode)

for i in range(0,len(b1)):
		
	if b1[i][1] == userboro:	
		zipcode = Zipcode(int(b1[i][0]))
				
		if str(zipcode.number) in zippop.keys():
			if zippop[str(zipcode.number)]!='':
				det=int(zippop[str(zipcode.number)])
			else:
				det=0
			zort=(zipcode.number,det)		
			boroughs[userboro].addZipCode(zort)

#averagec is the method in the class calculating the average population
print boroughs[userboro].averagec()
