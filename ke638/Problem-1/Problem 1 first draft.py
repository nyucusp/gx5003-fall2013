#enable array
import sys
i=sys.arvgv[1]# define i
j=sys.argv[2]#define j

for n in range (i,j)
    print n
sequence[]

def cycle_length(n):
    if n==1: 
        return 1
    elif n%2==0:
        return cycle_length(n/2)+1
    else:
        return cycle_length(3n+1)+1

def problem(i,j):
    return max([cycle_length(x) for x in range (i,j+1)])
        
