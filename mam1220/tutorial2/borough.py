######################################################################
#
# 	tutorial 2 - borough class
# 	September 21th, 2013
#
#	Michael Musick
#
######################################################################

class Borough(object):
	name = None
	zipcodes = None

	def __init__(self, name):
		self.name = name
		self.zipcodes = []

	def addZipcode(self, zip):
		self.zipcodes.append(zip)