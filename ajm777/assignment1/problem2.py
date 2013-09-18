#Aliya Merali
#Assignment 1 - Problem 2

import sys
ni = sys.argv[1:] #The list of n numbers
n  = int(sys.argv[1]) #n, the total amount of numbers 

#Creating the list to compare my values against 
standard = []
y  = 0
while  y < (n-1):
    y = y + 1
    standard.append(y)

#Creating a list of the differences in the input string
difflist = []
x = 1
while x<(n):
    diff = abs(int(ni[x])-int(ni[x+1]))
    difflist.append(diff)
    x = x+1

#Check if difflist = standard
set1=set(difflist)
set2=set(standard)
if set1==set2:
    print "Jolly"
else:
    print "Not Jolly"
