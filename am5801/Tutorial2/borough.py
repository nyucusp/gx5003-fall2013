# Awais Malik
# Assignment 2
# Tutorial 2
# borough.py

class Borough:
   name = None
   zipcodes = None
   
   def __init__(self, name):
     self.name = name
     self.zipcodes = []
 
   def addZipcode(self, zip):
     self.zipcodes.append(zip)
