#Nathan Seltzer
#Assignment 3
	#Problem 1

#the following creates a function that rounds number to two decimal points
def roundNumber(x):
	return int(100 * x)/100.0

"""open input1.txt file"""

input1 = open('input1.txt','r')

"""
(1)separate integers that signify N amount of students
(2)add up floats that follow until the next integer
and divide by N amount of students 
"""


num_students = []

sum_of_costs = []
fileLines = input1.readlines()
#print fileLines
sum_of_costs = fileLines

####################
import math #neccesary for absolute value function

lineIndex = 0
numberOfLines = len(fileLines)


while(lineIndex < numberOfLines):
	studentsCosts = []
	numberOfStudents = int(fileLines[lineIndex])
	if(numberOfStudents == 0):
		break
	# terminates at zero
	lineIndex = lineIndex + 1
	totalCost = 0
	#the following creates list of numbers following each integer
	for t in range(0,numberOfStudents): #from 0 until the number of students
		studentCost = float(fileLines[lineIndex])
		studentsCosts.append(studentCost)
		totalCost = totalCost + studentCost
		lineIndex = lineIndex + 1
	averageCost = totalCost / numberOfStudents
	# print averageCost
	# averageCost	= int(100 * averageCost)/100.0
	# print averageCost

	totalChange = 0
	for t in range(0,numberOfStudents):
		hasToPay = math.fabs(averageCost - studentsCosts[t])
		hasToPay = roundNumber(hasToPay)
		totalChange = totalChange + hasToPay
		#print hasToPay
	print totalChange/2.0	

### the rest of this file was my thinking process
"""
not sure how to exactly write the loop syntax, but the
following code would add up each float value and divide
by the number of students
"""

#blocking out the following so that the previous code runs properly

""""
mean = 0
n = 0
for number in input1:
	number = float(number)
	mean = mean + number
	n += 1
input1.close()
mean = mean/n
print mean
"""

"""
also not sure how to do this, but would have to write
an if/else statement that would prevent the program from
containing more than 1000 students or have an individual
spend more than $10,000
"""