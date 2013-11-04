class Borough:
    name = None
    zipcodes = None

    def __init__(self, name):
        self.name = name
        self.zipcodes = []

    def addZipcode(self, zip):
        self.zipcodes.append(zip)
