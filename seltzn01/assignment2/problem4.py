

# opens and reads borough.py and zipcode.py

myFile = open('c:\\Users\\Nathan\\desktop\\zipCodes.csv','r')

# import zipcode
from zipcode import Zipcode
from borough import Borough

boroughs = {}
myFile = open('c:\\Users\\Nathan\\desktop\\boroughs.csv','r')
for line in myFile:
	#print line
	tokens = line.split(',')
	value = tokens[0] # 0 refers to the firs column, zip code
	name = tokens[1].split('\n')[0] #.split('\n') removes stuff from borough name)
	print name
	zipcode = Zipcode(value)
	if name not in boroughs:
		borough = Borough(name)
		boroughs[name] = borough
	boroughs[name].addZipcode(zipcode)
print boroughs['Bronx'].zipcodes

""""the printout notes exactly where each instance of Bronx
is located in the memory"""