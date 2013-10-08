#Nathan Seltzer
#Assignment 3
	#Problem 1

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
print fileLines
sum_of_costs = fileLines

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