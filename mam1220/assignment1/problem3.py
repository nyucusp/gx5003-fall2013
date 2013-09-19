#!usr/bin/python

######################################################################
#
# Assignment 1 - Problem 3
# September 18th, 2013
#
# sample input:
#	python problem3.py "3 4 \n * . . . \n .** . \n *...\n 4 6 \n ****.. \n ..*..* \n ....**\n**..*."
#
######################################################################

# import a lib for system input
import sys 	# lib to get terminal input

# split the data up
lines = sys.argv[1]
matrixList = lines.split('\\n')

# print matrixList # test print

# get matrix sizes and number of matrices
fieldNum = 0		# number of minesweeper fields
fieldSize = []		# create a field size matrix
fieldSize.append([])# add a new matrix for the first field
expectNums = True	# expect nums for the current field size
for x in lines:					# look at every char in the data
	if x.isdigit() == True:		# if this is a digit
		if expectNums == False:	# I wasn't expecting another number to define size?
			fieldNum += 1 		# so that means there is another field
			fieldSize.append([])# create another field size matrix
			expectNums = True	# I am expecting another number to define this
		# append this value to the field size matrix
		fieldSize[fieldNum].append(int(x))
	# if this was a 'n' then it must not be a defining number
	if x == 'n':
		expectNums = False			

# work through the matrix list position grabbing each line
listPos = 0
print ""	# first print to separate output from input line

# work through each minesweeper field
for i in range(0, fieldNum+1):
	# create matrix filled with zeros and '*'s
	# print fieldSize[i][0], fieldSize[i][1], "minesweep field size" # test print
	matrix= []
	for x in range(0, fieldSize[i][0]):
		matrix.append(x)
		pos = []
		for d in matrixList[1+listPos]:
			if d == ".":	# if its a '.' put a 0
				pos.append(0)
			if d == "*":	# if its a '*' keep it
				pos.append('*')
		# add the array row to the minesweeper matrix
		matrix[x] = pos 	
		# next listPos
		listPos += 1 
	# account for size row in next minesweeper field
	listPos += 1 

	# print matrix # test print of zero'd matrix

	# look at each position in the matrix
	for x in range(0, fieldSize[i][0]):
		for y in range(0, fieldSize[i][1]):
			# if the position is a '*' then add a 1 to every box surrounding it
			if matrix[x][y] == "*":
				# get corners of the surrounding box
				if x == 0:
					top = 0
				else:
					top = x-1
				if x == fieldSize[i][0]-1:
					bot = fieldSize[i][0]-1
				else:
					bot = x+1
				if y == 0:
					left = 0
				else:
					left = y-1
				if y == fieldSize[i][1]-1:
					right = fieldSize[i][1]-1
				else:
					right = y+1

				# add the 1's
				for v in range(top, bot+1):
					for h in range(left, right+1):
						if matrix[v][h] != "*":
							matrix[v][h] += 1

	# print matrix # test print
	
	# print the minesweeper field
	# print fieldSize[i][0], fieldSize[i][1]
	print "Field #" + str(i+1) + ":"
	for x in range(0, fieldSize[i][0]):
		line = ''
		for y in matrix[x]:
			line += str(y)
		print line

	print ""
