class Borough:
  name = None
  zipcodes = []
  population = None
  zipCounter = 0

  def __init__(self, name):
    self.name = name
    self.zipcodes = []
    self.zipCounter = 0
    self.population = 0

  def addZipcode(self, zip):
    self.zipcodes.append(zip)
    self.zipCounter += 1
