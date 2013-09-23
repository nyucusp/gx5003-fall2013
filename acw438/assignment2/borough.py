class Borough:
    name = None
    zipcodes = None

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
