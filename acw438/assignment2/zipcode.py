class Zipcode:
    number = None
    population = 0
    incidents = 0
    area = 0
    counter = 0
    popCounter = 0
    
    def __init__(self, number, population, area=0):
        self.number = number
        if population != '':
            self.population = population
            self.popCounter += 1
        self.area = area
        self.counter += 1

    def addIncident(self, incidents):
        self.incidents += int(incidents)

    def passAttributes(self):
        pop = self.population
        inci = self.incidents
        self.population = 0 #reset population so it isn't counted twice
        self.incidents = 0 #reset incidents so they aren't counted twice
        self.popCounter += 1
        return pop, inci

    def avgFeatures(self, addlPop, addlArea):
        #add up total value of areas collected so far (for this zip):
        areaSum = (self.area * self.counter) + addlArea

        #divide by number of areas collected to get new average value:
        self.area = areaSum/(self.counter+1)

        #increment number of areas collected:
        self.counter += 1

        if addlPop != '':
            #add up total value of populations collected so far (for this zip):
            popSum = (self.population * self.popCounter) + addlPop

            #divide by number of populations collected to get new avg value:
            self.population = popSum/(self.popCounter + 1)

            #increment number of populations collected:
            self.popCounter += 1
            
    def densityCalc(self):
        return self.population/self.area
            
