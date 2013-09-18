import math
import sys

sequence =int(sys.argv[10])
n = len(sequence)
print n

for i in range(1,n):
    jolly = (math.fabs(inp[i]-inp[i-1]))


val = 0
for i in range (1,n):
    if out[i-1] == i:
        val = val + 1
if val == n-1:
    print "jolly"
else:
    print "not jolly"
