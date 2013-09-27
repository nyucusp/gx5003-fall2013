# Gang Zhao, Assignment 2, Problem 3
class Borough:
    name = None
    zipcodes = None
    populations = 0
    popcount = 0
    incidents = 0
    inpercap = 0
    popave = 0

    def __init__(self, name):
        self.name = name
        self.zipcodes = []
        
    def addZipcode(self, zip):
        self.zipcodes.append(zip)

    def addPopulation(self, population):
        self.populations += population
        self.popcount += 1

    def addIncident(self, incident):
        self.incidents += incident
   
    def incidentpercap(self):
        self.inpercap = self.incidents/float(self.populations)

    def popaverge(self):
        self.popave = self.populations/float(self.popcount)
    
