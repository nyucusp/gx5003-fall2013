#!usr/bin/python

# Assignment 1 - Problem 1
# September 18th, 2013


import sys 	# lib to get terminal input

# put the user supplied arguments into a list
pairList = [ int( sys.argv[1] ), int( sys.argv[2] ) ]	

# sort the list to ensure it is from lowest to highest order
pairList.sort()

# check every integer between the two input ints
num = pairList[0]
numList = []	# a place to store the final "total operation" values
while num <= pairList[1]:
	algNum = num 	# the current number being assessed by the algorithm
	num += 1 		# count upwards towards the second int 

	# print algNum	# test print

	# find the length of the algorithm
	opCount = 1 					# count the num of operations
									# start at '1' to account for final op
	while algNum != 1: 				# check while not equal to 1
		if algNum % 2 == 0:			# if even
			algNum /= 2
		elif algNum % 2 == 1:		# if odd
			algNum = algNum * 3 + 1

		opCount += 1				# increase the operation count
		# print algNum	# test print

	# # test prints
	# print " while done "	
	# print opCount
	# print " "

	# append the value to the list
	numList.append( opCount )

# print the information out
print pairList[0], pairList[1], max(numList) 