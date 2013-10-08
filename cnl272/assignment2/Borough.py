class Borough:
	name = None
	zipcodes = None
	average=None
	def __init__(self, name):
		self.name = name
		self.zipcodes = []
		self.average = 0

	def addZipcode(self, zpcode):
		self.zipcodes.append(zpcode)

	def count_average(self,population):
		self.average = float(population)/len(self.zipcodes)
	