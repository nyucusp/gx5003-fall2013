#Katherine Elliott
#Assignment  1 Problem 1

import sys
print sys.argv

n = 10
max = 0

def test(n):
    if (n%2 == 1):
        n=3*n+1 #n is odd
    else:
        n = n/2 #n is even
    return n

def cycle(n):
    global max
    count = 1   
    while n !=1:
        n =test(n)
        count += 1
    #print count

    if(count>max):
        max=count

i= int(sys.argv[1])
j= int(sys.argv[2])

for n in range(i,j+1):
    #print "Calculating cycle of "+str(n)
    cycle(n)

print str(i)+' '+str(j)+' '+str(max)

    
