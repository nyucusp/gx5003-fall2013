#!usr/bin/python

######################################################################
#
# 	Assignment 3 - Problem 1
# 	October 7th, 2013
#
# 	Michael Musick
#
######################################################################

import sys

# open the db file containing zipcodes for each borough
dbFile = open('input1.txt','r')

# read in the first line
tripSize = dbFile.readline()
# convert to an int
tripSize = int(tripSize)

# while trips are existing do this
while tripSize != 0:
	costs = []
	# for the size of the trip
	for i in range(tripSize):
		cost = dbFile.readline()				
		costs.append(float(cost))

	# find the sum and avg
	tripSum = sum(costs)	
	tripAvg = round( tripSum / tripSize, 2)
	
	# find the total amount exchanges
	totalExchange = 0
	for val in costs:
		if val < tripAvg:
			totalExchange += tripAvg - val

	# format and print
	print '$' + '%.2f' % totalExchange

	# get the next trip
	tripSize = int(dbFile.readline())
