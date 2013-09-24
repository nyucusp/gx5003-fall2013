import sys
import math

i = int(sys.argv[1])
j = int(sys.argv[2])
kk = i
max = 0

while kk>=i and kk<=j:
    k = kk
    myList=[]
    myList.append(kk)
    while k > 1:
        if k % 2 == 0:
            k=k/2
            myList.append(k)
        elif k%2 != 0:
            k=(k*3)+1
            myList.append(k)
    sizeOfList = len(myList)
    if sizeOfList > max:
        max = sizeOfList
    kk = kk+1
#print myList

print str(i) + " " + str(j) + " " + str(max)
            

# sum = i + j
# print 'the sum is ' + str(sum)
