#!usr/bin/python

# Assignment 1 - Problem 2
# September 18th, 2013


import sys 	# lib to get terminal input
print len(sys.argv) # test print


lines = sys.argv[1]
matrixList = lines.split('\\n')

print matrixList
print matrixList[1]