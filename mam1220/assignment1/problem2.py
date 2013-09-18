#!usr/bin/python

# Assignment 1 - Problem 2
# September 18th, 2013


import sys 	# lib to get terminal input
# print len(sys.argv) # test print

# put the user supplied arguments into a list
w = 1
intList = []
while w < len(sys.argv):
	intList.append( int( sys.argv[w] ) )
	w += 1

# find the first difference

# initialize jolly var
jolly = True

# find the first val
curDiff = abs( intList[0] - intList[1] )
# print curDiff # test print
# make sure the difference value is n-1
if curDiff != len(intList)-1:
	jolly = False

# if the first difference is correct, check the remaining
num = 1
while num < len(intList)-1 and jolly == True:
	nextDiff = abs( intList[num] - intList[num+1] )
	# print nextDiff # test print
	# if they are not sequential then its not a jolly jumper
	if nextDiff != curDiff-1:
		jolly = False
	# reassign and increment to next location
	else:
		curDiff = nextDiff
		num += 1

# if the last difference does not equal 1 then the list was too short
if curDiff != 1:
	jolly = False


# print statements
if jolly == True:
	print "Jolly"
else:
	print "not jolly"
