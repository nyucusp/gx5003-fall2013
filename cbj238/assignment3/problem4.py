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
	
	for y in xrange(gridArr.shape[0]):
		for x in xrange(gridArr.shape[1]):
			results = word_search_by_point(gridArr, words, y, x)
			for word in results:
				resultDict[word].append((y, x))

	process_results(words, resultDict)

def word_search_by_point(grid, words, y, x):
	results = []
	for word in words:
		if grid[y, x] == word[0]:
			if word_e(grid, word, y, x) or word_se(grid, word, y, x) or word_s(grid, word, y, x) or word_sw(grid, word, y, x) or word_w(grid, word, y, x) or word_nw(grid, word, y, x) or word_n(grid, word, y, x) or word_ne(grid, word, y, x):
				results.append(word)

	return set(results)

def word_e(grid, word, y, x):
	word_ind = 1
	y_ind = y
	x_ind = x + 1
	ret = False
	while x_ind < grid.shape[1]:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind += 1

	if debug and ret:
		print "Found {0} E ({1}, {2})".format(word, y, x)
	return ret

def word_se(grid, word, y, x):
	word_ind = 1
	y_ind = y + 1
	x_ind = x + 1
	ret = False
	while y_ind < grid.shape[0] and x_ind < grid.shape[1]:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind += 1
		y_ind += 1

	if debug and ret:
		print "Found {0} SE ({1}, {2})".format(word, y, x)

	return ret

def word_s(grid, word, y, x):
	word_ind = 1
	y_ind = y + 1
	x_ind = x
	ret = False
	while y_ind < grid.shape[0]:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		y_ind += 1

	if debug and ret:
		print "Found {0} S ({1}, {2})".format(word, y, x)
	return ret

def word_sw(grid, word, y, x):
	word_ind = 1
	y_ind = y + 1
	x_ind = x - 1
	ret = False
	while y_ind < grid.shape[0] and x_ind >= 0:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind -= 1
		y_ind += 1

	if debug and ret:
		print "Found {0} SW ({1}, {2})".format(word, y, x)

	return ret

def word_w(grid, word, y, x):
	word_ind = 1
	y_ind = y
	x_ind = x - 1
	ret = False
	while x_ind >= 0:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind -= 1

	if debug and ret:
		print "Found {0} W ({1}, {2})".format(word, y, x)

	return ret

def word_nw(grid, word, y, x):
	word_ind = 1
	y_ind = y - 1
	x_ind = x - 1
	ret = False
	while y_ind >= 0 and x_ind >= 0:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind -= 1
		y_ind -= 1

	if debug and ret:
		print "Found {0} NW ({1}, {2})".format(word, y, x)

	return ret

def word_n(grid, word, y, x):
	word_ind = 1
	y_ind = y - 1
	x_ind = x
	ret = False
	while y_ind >= 0:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		y_ind -= 1

	if debug and ret:
		print "Found {0} N ({1}, {2})".format(word, y, x)
	return ret

def word_ne(grid, word, y, x):
	word_ind = 1
	y_ind = y - 1
	x_ind = x + 1
	ret = False
	while y_ind >= 0 and x_ind < grid.shape[1]:
		if grid[y_ind, x_ind] == word[word_ind]:
			word_ind += 1
			if word_ind == (len(word)):
				ret = True
				break
		else:
			break

		x_ind += 1
		y_ind -= 1

	if debug and ret:
		print "Found {0} NE ({1}, {2})".format(word, y, x)
	return ret


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
				# if there's more than one first value, take the one with the lest second value
				if minValA == item[0]:
					if item[1] < minValB:
						minValB = item[1]
				elif (minValA == None) or (item[0] < minValA):
					minValA = item[0]
					minValB = item[1]
			result = (minValA, minValB)
		if result is not None:
			i, j = result
			print "{0} {1}".format(i+1, j+1)
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

