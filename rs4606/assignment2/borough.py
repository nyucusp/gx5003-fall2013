"""
We define a Borough class which has two attributes, name and a list of zipcodes.
"""

class Borough:
    name = None
    zipcodes = None
   
    def __init__(self, name):
        self.name = name
        self.zipcodes = []
 
    """
    This is a method that adds a zipcode to the "zipcodes" list attribute
    """ 
 
    def addZipcode(self, zip):
        self.zipcodes.append(zip)

    """
    Here we define the method to calculate the average population of all zip codes
    in an object of the Borough class.  We assume that the "zipcodes" list attribute
    in the Borough object is a list of Zipcode objects from the Zipcode class.
    """

    def avgpop(self):
        totalpop = 0
        num_zips = len(self.zipcodes)
        for zip in self.zipcodes:
            totalpop += zip.population
        print totalpop/num_zips