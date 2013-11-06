class Borough:
    name = None
    zipcodeList = None

    def __init__(self, name):
        self.name = name
        self.zipcodeList = []

    def addZipcode(self, zip):
        self.zipcodeList.append(zip)

    def getAvgPopulation(self):
        totalArea = 0
        totalPopulation = 0
        for zip in self.zipcodeList:
            totalArea += zip.zipArea
            totalPopulation += zip.zipPopulation

        return totalPopulation / totalArea
