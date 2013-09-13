import sys
import math

# A sequence of n > 0 integers is called a jolly jumper if the absolute values of the differences between successive elements take on all possible values 1 through n - 1. For instance,

# 1 4 2 3

# is a jolly jumper, because the absolute differences are 3, 2, and 1, respectively. The definition implies that any sequence of a single integer is a jolly jumper. Write a program to determine whether each of a number of sequences is a jolly jumper.

# Input

# Each line of input contains an integer n < 3, 000 followed by n integers representing the sequence.

# Output

# For each line of input generate a line of output saying ``Jolly'' or ``Not jolly''.

#generate 1 through n - 1

maxValue = 1

for i in range(1,len(sys.argv)):
  if (sys.argv[i] > maxValue):
    maxValue = sys.argv[i]


print maxValue

# #Take in integer string
# for i in range(len(sys.argv)):
#   if (fabs(int(sys.argv[i]) - int(sys.argv[i+1]) > )

# #calc and test successive absolute differences


# print "Jolly"

# print "Not jolly"