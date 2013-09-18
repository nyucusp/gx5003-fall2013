import sys
import math

input = sys.argv
input.pop(0)

"""
Here input1 is the actual sequence (the entries are strings, however), and length
is an integer representing the length of the sequence
"""


input1 = input[0].split()
length = int(input1.pop(0))

"""
Here we make a list which has all differences from 1 to length-1
"""

potential_differences = []
for i in range(1, length):
    potential_differences.append(i)

"""
Here we make a list which has the absolute values of all (length-1) differences 
from the input sequence
"""

list_of_differences = []
for i in range(0, length-1):
    list_of_differences.append((abs(int(input1[i])-int(input1[i+1]))))

"""
Here we compare the two lists (the second one is sorted)
"""

if sorted(list_of_differences) == potential_differences:
    print "Jolly"
else: 
    print "Not Jolly"

