class Borough:
   name = None
   zipcodes = None
   
   def __init__(self, name):
     self.name = name
     zipcodes = []
 
   def addZipcode(self, zip):
     zipcodes.append(zip)

class Zipcode:
    number=None

    def _init_(self,number):
        self.number=number
