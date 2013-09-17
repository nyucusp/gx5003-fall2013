
import sys

i = int(sys.argv[1])
j = int(sys.argv[2])
r=i
count=0
cyclelog = []

while (i<=r and r<=j):
    n = r
    cycle=0

    while(1<n and n<=1000000):
        if n%2==0:
            n=n*0.5
            cycle=cycle+1
        else:
            n=(3*n)+1
            cycle=cycle+1
   
    cyclem=cycle+1
    cyclelog.append(cyclem)
    r=r+1

print str(i), str(j), max(cyclelog)
