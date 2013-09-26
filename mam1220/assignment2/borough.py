######################################################################
#
# 	problem 4 - borough class
# 	September 21th, 2013
#
#	Michael Musick
#
######################################################################

class Borough(object):
	name = None
	zipcodes = None
	avgPop = None
	totPop = 0
	totAreaSize = 0

	def __init__(self, name):
		self.name = name
		self.zipcodes = {}

	def addZipcode(self, zipnum):
		# create a dictionary item to store info
		self.zipcodes[zipnum] = {'population': 0, 'area': 0}

	def modify_Pop_Area(self, zipnum, pop, area):
		# modify the entry
		if zipnum in self.zipcodes:
			self.zipcodes[zipnum] = {'population': pop, 'area': area}		

	def getAvgPop(self):
		# get the average population
		self.totAreaSize = 0
		self.totPop = 0
		for zipnum in self.zipcodes:
			self.totPop += self.zipcodes[zipnum]['population']
			self.totAreaSize += self.zipcodes[zipnum]['area']
		self.avgPop = self.totPop / self.totAreaSize
		return self.avgPop

	def avgPopStr(self):
		# return a string
		self.getAvgPop()
		return "The average population of " + self.name + " is " + str(self.avgPop) + " people per the unspecified unit of measurement."