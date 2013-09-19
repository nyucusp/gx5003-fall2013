import sys
import math

jollyValue = True

n = int(sys.argv[1])
inp = sys.argv[2:]
intList = map(int, inp)    # map integers to list
out = []


for i in range(1, n):
    out.append(math.fabs(inp[i] - inp[i - 1]))
out.sort()
val = 0
    
for i in range(1, n):
    if out[i - 1] == i:
            val = val + 1

if val == n - 1:
    print "Jolly"
else:
    print "Not Jolly"