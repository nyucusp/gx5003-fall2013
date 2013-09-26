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

    def avgZipPop(self):
        boroughPop = 0
        zipCount = 0
        for line in self.zipcodes:
            boroughPop += int(line.population)
            zipCount += 1
        return boroughPop/zipCount

    def addPopInst(self, addlTuple):
#        print addlTuple
        if addlTuple[0] != '':
            self.totalPop += int(addlTuple[0])
        self.totalIncidents += int(addlTuple[1])

    def calcInstPopAvg(self):
        floatPop = float(self.totalPop)
        return floatPop/self.totalIncidents
