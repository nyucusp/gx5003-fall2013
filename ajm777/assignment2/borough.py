class Borough:
    name = None
    zipcodes = None
    totalPop = None
    numZips = None
    avg = None


    def __init__(self, name):
        self.name = name
        self.zipcodes=[]

    def addZipcode(self, zip):
        self.zipcodes.append(zip)

    def calcAvgPop(self, totalPop, numZips):
        self.avg = totalPop/numZips 
