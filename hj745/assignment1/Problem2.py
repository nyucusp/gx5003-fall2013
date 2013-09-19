import math

n = 4
inp = [1,4,2,3]
oup = []

for i in range(1,n):
    oup.append(math.fabs(inp[i]-inp[i-1]))
oup.sort()
val = 0

for i in range(1,n):
    if oup[i-1] == i:
        val = val+1
if val == n-1:
    print "jolly"
else:
    print "not jolly"