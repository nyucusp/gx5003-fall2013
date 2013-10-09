class Borough:
    name = None
    zipcodes = None
    
def __init__(self, name):
    self.name = name
    self.zipcodes = []
    
def addZipcode(self,zip):#list of zipcodes added to class
    self.zipcodes.append(zip)

def avgPop(self):#sum of population/ number of zip code entries to compute average population
    totalpop = 0
    num_zipcodes = len(self.zipcodes)
    for zip in self.zipcodes:
        totalpop += zip.population
    print totalpop/num_zipcodes