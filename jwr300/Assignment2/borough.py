#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Tutorial 2
#Creates the Borough Class

class Borough:
	name = None
	zipcodes = None

	def __init__(self, name):
		self.name = name
		self.zipcodes = []

	def averagePopulation(self):
		average = 0
		sumPop = 0
		zip_count = len(self.zipcodes)
		for zip in self.zipcodes:
			sumPop += zip.population

		average = sumPop/zip_count
		return average

	def addZipcode(self, zip):
		self.zipcodes.append(zip)