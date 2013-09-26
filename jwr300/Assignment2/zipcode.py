#!/usr/local/bin/python
#Warren Reed
#Principles of Urban Informatics
#Assignment 2, Tutorial 2
#Creates the zipcode Class with two attributes, the zip code number
# and the population of the zipcode

class Zipcode:
	number = None
	population = None

	def __init__(self, number, population):
		self.number = number
		self.population = population


