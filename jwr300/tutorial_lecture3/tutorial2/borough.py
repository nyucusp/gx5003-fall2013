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

	def addZipcode(self, zip):
		zipcodes.append(zip)