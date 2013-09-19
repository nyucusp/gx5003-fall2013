#Kara Leary
#Assignment 1 - Problem 1
#Urban Informatics

import sys
firstParameter = int(sys.argv[1])
secondParameter = int(sys.argv[2])


def ncycles(x):
	n=0
	while int(x)!=1:
		if x%2==0:
			x=x/2
		elif x%2==1:
			x=(x*3)+1
		n=n+1
	if x==1:
		n=n+1
	return n

x = firstParameter
countmax = 0
for x in range(firstParameter, secondParameter):
	count = ncycles(x)
	if count > countmax:
		countmax = count
	x+=1

print firstParameter, secondParameter, countmax