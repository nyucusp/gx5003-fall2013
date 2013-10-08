#!usr/bin/python

######################################################################
#
# 	Assignment 3 - Problem 2
# 	October 7th, 2013
#
# 	Michael Musick
#
######################################################################

import sys

# open the db file containing zipcodes for each borough
dbFile = open('input2.txt','r')

numOfCases = int(dbFile.readline())
# do away with the empty line
dbFile.readline()

# print numOfCases

# do for the number of cases
for _ in xrange(numOfCases):
	# next line is number of candidates
	numOfCandidates = int(dbFile.readline())
	# print "number of candidates: " + str(numOfCandidates)

	# create a candidate dictionary and fill it up
	candDict = {}
	for num in xrange(numOfCandidates):
		cand = (dbFile.readline()).strip()
		dictC = {'candidate': cand, 'votes': 0, 'perc': 0}
		candDict[num+1] = dictC

	# print candDict

	# work through the ballots
	ballotArray = []
	ballotTot= 0
	ballot = dbFile.readline()
	# if this is the blank line there are no more ballots
	while ballot != '\n' and len(ballot) > 1:
		# keep track of ballots for perc
		ballotTot += 1
		# make the ballot an array and add to main ballot array
		ballot = ballot.strip().split(' ')
		ballotArray.append(ballot)
		
		# assign values to candidates 
		topCand = int(ballot[0])
		candDict[topCand]['votes'] += 1

		# get next ballot
		ballot = dbFile.readline()

	# print "ballot total: "+ str(ballotTot)

	# initialize test variables
	winnerFound = False
	minVotes = 1001

	# look at each candidate and calculate their percentage and track min votes
	for key in candDict:
		votes = float(candDict[key]['votes'])
		if votes < minVotes:
			minVotes = votes
		perc = votes / float(ballotTot)
		candDict[key]['perc'] = perc
		# if someone has more than 50% they
		if perc > 0.5:
			winnerFound = True

	# print "initial candDict: " + str(candDict)
	# print "minVotes: " + str(minVotes)
		
	# if winner was not found on first attempt work through ballots according to rules	
	while winnerFound != True:
		loserCands = []
		# delete the losers from the dict
		for key in candDict:
			if candDict[key]['votes'] == int(minVotes):
				loserCands.append(key)
				# print "loser: " + str(candDict[key])
		# print "loserCands: " + str(loserCands)

		# if the loser length equals the remaining candidates then declear a winner
		if len(loserCands) == len(candDict):
			winnerFound = True
		# else remove them from the dict
		else:
			for i in loserCands:
				if i in candDict:
					del candDict[i]
		# if only one remains he wins!
		if len(candDict) == 1:
			winnerFound = True
			break

		# get the new minvote number
		minVotes = 1001
		for ballot in ballotArray:						
			pos = 0
			keepLooking = True
			# check if this ballot is one that already picked a loser
			while int(ballot[pos]) not in candDict and keepLooking == True:
				# if so did they pick a loser in this round
				# if so count ballots who picked a loser
				if int(ballot[pos]) in loserCands:
					while pos != -1:
						topCand = int(ballot[pos])
						if topCand in candDict:				
							candDict[topCand]['votes'] += 1
							votes = candDict[topCand]['votes']
							pos = -1
							perc = float(votes) / float(ballotTot)
							candDict[topCand]['perc'] = perc
							if perc > 0.5:
								winnerFound = True							
						else:
							pos += 1
					keepLooking = False
				# if it was not in the loser list for this position increment and was also not in 				
				pos += 1

		# get the new min
		if winnerFound != True:
			for key in candDict:
				votes = candDict[key]['votes']
				if votes < minVotes:
					minVotes = votes
		

	# print the results
	for key in candDict:
		print candDict[key]['candidate']
	print