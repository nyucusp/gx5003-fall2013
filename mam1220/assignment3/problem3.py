#!usr/bin/python

######################################################################
#
# 	Assignment 3 - Problem 3
# 	October 7th, 2013
#
# 	Michael Musick
#
######################################################################

import sys

# open the db file containing zipcodes for each borough
dbFile = open('input3.txt','r')

scenarioNum = int(dbFile.readline())
# print scenarioNum

for scenario in xrange(scenarioNum):

	tempSizes = dbFile.readline()
	tempSizes = tempSizes.strip().split(' ')
	paperDB_size = int(tempSizes[0])
	nameDB_size = int(tempSizes[1])


	paperDB = {}
	for num in xrange(paperDB_size):
		line = dbFile.readline()
		line = line.strip().split(':')
		line = line[0]
		line = line.strip().split('., ')
		# add the dote to the back of each name I just removed
		numOfAuthor = len(line)
		for name in xrange(numOfAuthor-1):
			line[name] = line[name] + '.'
		paperDB[num] = line

	nameDB = {}
	printOrder = []
	for num in xrange(nameDB_size):
		line = dbFile.readline()
		line = line.strip('\n')
		nameDB[line] = None
		printOrder.append(line)

	# print paperDB	
	# print nameDB
	# print printOrder

	# create a DB for other authors
	othersDB= {}

	# create an array of papers to delete that have been checked
	toDel = []

	# find those who have published with erdos
	for paper in paperDB:
		if 'Erdos, P.' in paperDB[paper]:
			for name in paperDB[paper]:
				if name in nameDB:
					nameDB[name] = 1
				else: 
					# check if it is in the othersDB
					if name not in othersDB:
						othersDB[name] = 1
			toDel.append(paper)

	# del the papers with erdos
	for i in toDel:
		del paperDB[i]



	# check the next num
	foundConnection = True
	# continue while a connection was found
	while foundConnection == True:
		toDel = []
		for paper in paperDB:
			authorslist =  paperDB[paper]
			
			# check the name if each person in the paper for an erdos num
			erdosNum = None
			for name in authorslist:
				# if it is in the mainDB, does it have a number yet		
				# if it is in the othersDB, does it have a number yet
				if name in othersDB:			
					theirNum = othersDB[name]
					if erdosNum == None:
						erdosNum = theirNum
					else:
						if theirNum < erdosNum and erdosNum == None:						
							erdosNum = theirNum
				else:
					if name in nameDB:
						if nameDB[name] is not None:
							theirNum = nameDB[name]
							if erdosNum == None:							
								erdosNum = theirNum
							if theirNum < erdosNum:
								erdosNum = theirNum
					else:
						if name not in othersDB:
							othersDB[name] = None					
				# print name + str(erdosNum)
			# add the erdos numbers
			if erdosNum != None:
				erdosNum += 1
				for name in authorslist:
					if name in nameDB:
						if nameDB[name] == None:
							nameDB[name] = erdosNum
						if nameDB[name] > erdosNum:
							nameDB[name] = erdosNum
						
					else:
						if name in othersDB:
							if othersDB[name] == None:
								othersDB[name] = erdosNum
							if othersDB[name] > erdosNum:
								othersDB[name] = erdosNum
						else:
							othersDB[name] = erdosNum

				toDel.append(paper)
			# else:
			# 	foundConnection = False	


		# del the papers with erdos
		if len(toDel) > 0:
			for i in toDel:
				if i in paperDB:
					del paperDB[i]
		else:
			foundConnection = False

	print "Scenario " + str(scenario)
	# reverse that dict
	printDict = {}
	for name in printOrder:
		if nameDB[name] == None:
			print name + " " + "infinity"
		else:
			print name + " " + str(nameDB[name])

	# get the next blank line before the next iteration
	line = dbFile.readline()
