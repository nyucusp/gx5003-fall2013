class Borough:
   name = None
   zipcodes = None
   sumpopul = None
   
   def __init__(self, name):
     self.name = name
     self.zipcodes = []
     self.sumpopul = 0

# here we have zip :[(zipcode,population in the zip code)] 
   def addZipcode(self, zip):
     self.zipcodes.append(zip[0][0])
     self.sumpopul += zip[0][1]

#average population calculator

   def averagec(self):
     sum=0	
     for i in range(0,len(self.zipcodes)):
	sum+=self.zipcodes[i][1] 	     
     return sum/i

