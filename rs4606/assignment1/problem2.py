import sys
import math

input = sys.argv
input.pop(0)
length = int(input[0])

count = 0

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

