'''
Christopher B. Jacoby
Urban Informatics
Homework 3, Problem 2
'''

import sys
import numpy as np
from readInputFile import Problem2Input

debug = False
if len(sys.argv) > 1:
	debug = True

def compute_election_winner_for_case(case):
	electionReturn = None
	done = False

	candidates = case[0]
	votes = case[1]
	
	i = 0
	while not done:
		(done, electionReturn, percentages) = calculate_round_winner_index([x[0] for x in votes])
		if debug:
			print "Vote round:", i+1, "\n\tResults:", electionReturn, "\n\tPercent:", percentages*100

		if not done:
			eliminate_tied_candidates(candidates, votes, percentages)

		i += 1
		# There are never more than 20 candidates, so we should never have more than 20 individual votes.
		# This is here just to avoid infinite loops, basically.
		if i > 20:
			break

	return np.array(candidates)[electionReturn]

def calculate_round_winner_index(round):
	'''
	Given an array containing the votes for a single runoff round 
	(which is to say after eliminations), calculate the winner.

	# Case 1... One persone is in the lead, >50%
	# Case 2... No one is >50%.
	'''
	bDone = False
	selectedCandidate = ()

	roundVotes = np.array(round)
	voteCounts = np.bincount(roundVotes)
	totalVotes = len(roundVotes)

	# zip(voteIdxs, voteCounts[voteIdxs])
	# Calculate the percentages for each
	votePercentages = voteCounts[1:] / float(totalVotes)

	# See how many wins there are:
	wins = votePercentages > 0.5
	if (wins).sum() == 1:
		bDone = True
		# The winner is the highest vote percentage
		selectedCandidate = votePercentages.argmax()
	else: # No one got more than 50%...
		bDone = False
		# The current winners are the ones with the highest vote percentages
		selectedCandidate = votePercentages == votePercentages.max()

	return (bDone, selectedCandidate, votePercentages)

def eliminate_tied_candidates(candidates, runoffMatrix, percentages):
	'''
	If there are candidates tied for last, remove them from the options
	'''
	# Find the candadites with the smallest percentage. (1 or more)
	# ** I am assuming that I am throwing out people with zero votes anyway, since
	# once I remove them, they get zero votes, and otherwise it would break my approach.
	removeIndecies = (percentages == percentages[percentages.nonzero()].min()).nonzero()[0]
	if debug:
		print "Removing: ", removeIndecies

	try:
		for vote in runoffMatrix:
			for candInd in removeIndecies:
				# This is +1 because candInd is 0-based and the voting system is 1-based
				vote.remove(candInd + 1)
	except ValueError:
		print "Vote (", vote, ") is missing", candInd+1

	if debug:
		print "\teliminating: ", np.array(candidates)[removeIndecies]
		print "New matrix: \n", np.array(runoffMatrix)


voteExamples = Problem2Input()
if debug:
	print "There are ", len(voteExamples.data), "cases to follow:"

	# print voteExamples.data

for case in voteExamples.data:
	if debug:
		print "====== New Election ======="
		print "Candidates: ", case[0]
	winner = compute_election_winner_for_case(case)

	if debug:
		print "Election Winner(s):",
	print winner
	print         # Adds a blank line after the results

