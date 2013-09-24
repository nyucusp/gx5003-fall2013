#!usr/bin/python

######################################################################
#
# tutorial 2 - borough class
# September 21th, 2013
#
######################################################################

class Borough:
	name = None
	zipcodes = None

	def __init__(self, name):
		self.name = name
		zipcodes = []

	def addZipcode(self, zip):
		zipcodes.append(zip)