#Receive import in the command line
import sys

#Define the cycle length function cl()
def cl(n):
    count=1
    while n!=1:
        if n%2==0:
            n=n/2
            count=count+1
        else:
            n=3*n+1;
            count=count+1
    return count

#Get the maximum cycle length
max=0
for x in range (int(sys.argv[1]),int(sys.argv[2])+1):
    if cl(x)>max:
        max=cl(x)

#Output        
print int(sys.argv[1]), int(sys.argv[2]),  max
