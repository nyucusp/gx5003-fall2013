#Kara Leary
#Assignment 1 - Problem 2
#Urban Informatics

import sys
n = int(sys.argv[1])

for i in xrange(1,n-1):
	jcount=0
	for j in xrange(2,n+1):
		var1=int(sys.argv[j])
		var2=int(sys.argv[j+1])
		if abs(var1-var2)==i:
			break
		else:
			jcount=jcount+1
		if jcount==n-1:
			print("Not Jolly")
			sys.exit()

print("Jolly")