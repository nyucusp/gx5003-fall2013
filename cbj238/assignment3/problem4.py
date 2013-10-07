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
				print "Found Forward Hor:", rowIndex, findForwards
			if findBackwards >= 0:
				resultDict[word].append((rowIndex, len(findBackwards) - 1 - findBackwards))
				print "Found Backwards Hor:", rowIndex, len(findBackwards) - 1 - findBackwards

def construct_horizontals(grid):
	return [x for x in grid]

def construct_verticals(grid):
	return [x for x in grid.T]

def construct_diagonals(grid):
	ret = []

	# Top Left to bottom right diagonals
	# Get the diagonals for y:[0,len]
	# for y in xrange(len(grid)):
	# 	for x
	# Get the diagonals for x:[1,len]

	# Top right to bottom left diagonals
	# get diagonals for y:[len:1]
	# get diagonals for x:[len:0]


	return ret

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

