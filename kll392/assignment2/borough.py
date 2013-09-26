class Borough:
    name = None
    zipcodes = None
    populations = 0
    populationcount = 0
    average = 0
    
    def __init__(self, name):
        self.name = name
        self.zipcodes = []

    def addZipcode(self, zipcode):
        self.zipcodes.append(zipcode)

    def addPopulation(self, population):  
    #addPopulation keeps a running total of the borough's population, 
    #as well as keeps track of how many times population has been added 
    #in order to have a value over which to compute the average.
        self.populations += population
        self.populationcount += 1

    def findAverage(self):
        self.average = (self.populations)/(self.populationcount)
