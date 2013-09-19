import math
n = int(input("Number of integers?"))
x = raw_input("Numbers seperated by space?")
inp = map(int, x.split())
for i in range(1,n):
        out.append(math.fabs(inp[i]-inp[i-1]))
out.sort()
val = 0
for i in range(1,n):
        if out[i-1] == i:
                val = val+1
if val == n-1:
        print "jolly"
else:
        print "not jolly"
