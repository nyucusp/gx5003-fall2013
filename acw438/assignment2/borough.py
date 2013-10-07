class Borough:
    name = None
    zipcodes = None
    totalIncidents = 0
    totalPop = 0

    def __init__(self, name):
        self.name = name
        self.zipcodes = []

    def addZipCode(self, zip):
        self.zipcodes.append(zip)

    #calculate population/zipcode:
    def avgZipPop(self):
        boroughPop = 0
        zipCount = 0
        for line in self.zipcodes:
            #add zip population to total population
            boroughPop += int(line.population)
            #increment count of zips
            zipCount += 1
        print boroughPop
        return boroughPop/zipCount

    #add incidents and population to counters 
    #(or only incidents if population field is empty)
    def addPopInst(self, addlTuple):
        if addlTuple[0] != '':
            self.totalPop += int(addlTuple[0])
        self.totalIncidents += int(addlTuple[1])

    #calculate incidents/population ratio
    def calcIncdPopRatio(self):
        floatPop = float(self.totalPop)
        return self.totalIncidents/floatPop
