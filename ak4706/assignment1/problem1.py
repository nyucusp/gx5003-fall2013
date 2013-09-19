import sys
import math

i = int(sys.argv[1])
j = int(sys.argv[2])
k = i
max = 0


while k>=i and k<=j:
    L=[]
    while k > 1:
        if k % 2 == 0:
            k=k/2
            L = L.append(k)
        elif k%2 != 0:
            k=(k*3)+1
            L = L.append(k)
        elif k in range(i,j+1):
            length = len(L)
            if(length > max):
                max = length
        k = k+1
print max
            

sum = i + j
print 'the sum is ' + str(sum)
