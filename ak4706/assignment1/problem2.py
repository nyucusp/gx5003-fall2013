import math
import sys

#First got it to work for a specific case and then generalized it
#Needed to get it to take the inputs as the length and then the rest of the numbers
# and then mapped the numbers into a list        
#sequence =[1,4,2,3]
n = int(sys.argv[1])
sequence = sys.argv[2: ]
inplist = map(int,sequence)

#n = 4
#n = len(sequence)
#print n

#adding the absolute values of the difference of all the numbers into a list
jolly = []
for i in range(1,n):
    jolly.append(math.fabs(int(sequence[i])-int(sequence[i-1])))

# adding constraints of when is Not Jolly, and all other times is jolly
isJolly = True
for i in range (1,n):
    if(not (i in jolly)):
        isJolly = False

if(len(jolly) != (n-1)):
    isJolly = False

if isJolly:
    print "Jolly"
else:
    print "Not Jolly"
