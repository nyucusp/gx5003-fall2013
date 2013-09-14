import sys
import math

# A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. For instance,

# 1 4 2 3

# is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper.

# Input

# Each line of input contains an integer n < 3,000 followed by n integers representing the sequence.

# Output

# For each line of input generate a line of output saying ``Jolly'' or ``Not jolly''.


maxValue = 1 #declare variable to hold maximum value in n integer string
jollyFlag = True

for i in range(1,len(sys.argv)): #loop through argument array from index 1 to the end
  if (sys.argv[i] > maxValue):
    maxValue = sys.argv[i]

maxValue = maxValue - 1 #set maxValue to n-1 

#Test each interval for absolute value greater than n-1
for i in range(len(sys.argv)):
  if (fabs(int(sys.argv[i]) - int(sys.argv[i+1]) > maxValue)):
    jollyFlag = False

#Test output from loop
if (jollyFlag == True):
  print "Jolly"
else:
  print "Not jolly"