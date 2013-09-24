class Borough:
    name = None
    zipcodes = None

    def __init__(self, name):
        self.name = name
        self.zipcodes = []

    def addZipCode(self, zip):
        self.zipcodes.append(zip)
