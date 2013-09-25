import sys
import csv  

class Borough:
   name = None
   zipcodes = None
   numOfZip=None
   population=None
   
   def __init__(self, name):
     self.name = name
     self.zipcodes = []
     self.numOfZip=0
     self.population=0
 
   def addZipcode(self, zip):
     self.zipcodes.append(zip)
     self.numOfZip+=1
     self.population+=zip.population

class Zipcode:
    number = None
    population =None
    
    def __init__(self, number, population):
        self.number = number
        self.population = population

boroFileRaw = open('boroughs.csv','r') # open borough file
boroFile=csv.reader(boroFileRaw, delimiter=',')

zipList=[] #define a list of concerned zip areas
for line in boroFile: # input the borough info to zipDict
    if line[1]==sys.argv[1]:
        zipList.append(line[0])

boroFileRaw.close()

zipFileRaw = open('zipCodes.csv','r') #open the zip file
zipFile=csv.DictReader(zipFileRaw, delimiter=',')

borough=Borough(sys.argv[1])#instantiate borough

for line in zipFile:# instantiate the zip areas concerned
   if (line['Total Population per ZIP Code']!=''):
       pop=int(line['Total Population per ZIP Code'])
       num=str(line['zip code tabulation area'])
       if num in zipList:
           zipcode=Zipcode(num,pop)
           borough.addZipcode(zipcode)
zipFileRaw.close()

if borough.numOfZip==0:
    print('Borough not found!Please try again!')
else:
    avgpop=int(borough.population/borough.numOfZip)
    print("The average ZIP population of "+sys.argv[1]+"is:"+str(avgpop)+".")
