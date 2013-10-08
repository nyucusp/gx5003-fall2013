'''
Christopher B. Jacoby
Urban Informatics
Homework 3, Problem 4
'''

import sys
import numpy as np
from readInputFile import Problem4Input

def search_grid_for_words(grid, words):
	gridArr = np.array(grid)
	resultDict = dict(zip(words, [[] for x in words]))
	search_arrays_for_words(construct_horizontals(gridArr), words, resultDict)
	search_arrays_for_words(construct_verticals(gridArr), words, resultDict)
	search_arrays_for_words(construct_diagonals(gridArr), words, resultDict)

	process_results(words, resultDict)

def search_arrays_for_words(arrays, words, resultDict):
	for rowIndex in xrange(len(arrays)):
		for word in words:
			row = arrays[rowIndex].tostring()
			findForwards = row.find(word)
			# to see if it's there backwards, we reverse the string... but then we have to
			# subtract the result from the index.
			findBackwards = row[::-1].find(word)

			if findForwards >= 0:
				resultDict[word].append((rowIndex, findForwards))
				print "Found Forward:", word, rowIndex, findForwards
			if findBackwards >= 0:
				resultDict[word].append((rowIndex, len(row) - 1 - findBackwards))
				print "Found Backwards:", word, rowIndex, len(row) - 1 - findBackwards

def construct_horizontals(grid):
	return [x for x in grid]

def construct_verticals(grid):
	return [x for x in grid.T]

def construct_diagonals(grid):
	ret = []

	# Top Left to bottom right diagonals
	# Get the diagonals for y:[0,len]
	diagList = []
	for y in xrange(len(grid)):
		diagList.append(get_diagonal_from_start(grid, y, 0))
		
	for x in xrange(len(grid[0])):
		diagList.append(get_diagonal_from_start(grid, 0, x))

	# Top right to bottom left diagonals
	for y in xrange(len(grid)):
		diagList.append(get_diagonal_from_start(grid, y, len(grid[y]), -1))
		
	# Get the diagonals for x:[1,len]
	for x in xrange(len(grid[0])):
		diagList.append(get_diagonal_from_start(grid, len(grid), x, -1))


	return ret

def get_diagonal_from_start(grid, y, x, dir=1):
	pass

def process_results(words, resultDict):
	'''
	remove the duplicates from the dict if there are any. Otherwise, just return the required strings.
	'''
	for key in words:
		result = None
		if len(resultDict[key]) == 1:
			result = resultDict[key][0]
			
		elif len(resultDict[key]) > 1:
			# If there's more than one, take the one with the min first value
			minValA = None
			minValB = None
			for item in resultDict[key]:
				if (minValA is None) or (item[0] < minValA):
					minValA = item[0]
					minValB = item[1]
				# if there's more than one first value, take the one with the lest second value
				elif minValA is item[0]:
					if item[1] < minValB:
						minValB = item[1]
		if result is not None:
			i, j = result
			print "{0} {1}".format(i, j)
		else:
			print "Error! Word not found"

debug = False
if len(sys.argv) > 1:
	debug = True

gridCases = Problem4Input()
if debug:
	print "There are ", len(gridCases.data), "cases to follow:"

	print gridCases.data

for case in gridCases.data:
	search_grid_for_words(case[0], case[1])

	if debug:
		print "====== New Case ======="
		print "Lines, Letters: ({0}): ".format(case[0])

	print         # Adds a blank line after the results

