import sys
import math

input = sys.argv
input.pop(0)
length = int(input[0])

count = 0

"""
In the following loop, i runs through the range from 1 to the length of the input
integer minus 1.  We compare it to each difference in the sequence in turn in 
the 'if' statement.  We use the dummy variable s to exit the while loop, and 
we increment the variable count to see how many differences match with our
variable i.
"""

for i in range(1,length):
    s = 0
    while s == 0:
        for j in range(1,length):        
            if i == math.fabs(int(input[j]) - int(input[j+1])):
                count += 1
                s += 1
        else: 
            s += 1
            
if count == length-1:
    print "Jolly"
else:
    print "Not Jolly"

