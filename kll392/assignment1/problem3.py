#Kara Leary
#Assignment 1 - Problem 3
#Urban Informatics

import sys
import numpy
import array
lines=sys.argv[1]
newlines = lines.split('\\n')

nm = newlines[0]
n = int(nm[0])
m = int(nm[2])

array=numpy.zeros((n,m))

for i in xrange(1,n+1):
	currentline=newlines[i]
	for j in xrange(0,m):
		currentspot=currentline[j]
		if currentspot=='*':
			if i==1:
				array[i,j]+=1
				if j!=0:
					array[i-1,j-1]+=1
					array[i,j-1]+=1
				if j!=m-1:
					array[i-1,j+1]+=1
					array[i,j+1]+=1
			elif j==0:
				array[i-1,j+1]+=1
				if i!=1:
					array[i-2,j+1]+=1
					array[i-2,j]+=1
				if i!=n:
					array[i,j]+=1
					array[i,j+1]+=1
			elif i==n:
				array[i-2,j]+=1
				if j!=0:
					array[i-2,j-1]+=1
					array[i-1,j-1]+=1
				if j!=m-1:
					array[i-2,j+1]+=1
					array[i-1,j+1]+=1
			elif j==m-1:
				array[i-1,j-1]+=1
				if i!=1:
					array[i-2,j-1]+=1
					array[i-2,j]+=1
				if i!=n:
					array[i,j-1]+=1
					array[i,j]+=1	
			else:
				array[i-2,j-1]+=1
				array[i-2,j]+=1
				array[i-2,j+1]+=1
				array[i-1,j-1]+=1
				array[i-1,j+1]+=1
				array[i,j-1]+=1
				array[i,j]+=1
				array[i,j+1]+=1


count=0
print 'Field #1'
for i in range(0,n):
	currentline=newlines[i+1]
	count=0
	for j in range(0,m):
		currentspot=currentline[j]
		if currentspot=='*': 
			print "*",
		else: 
			print int(array[i,j]),
		count+=1
		if count==m:
			print ''
			


