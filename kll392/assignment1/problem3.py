#Kara Leary
#Assignment 1 - Problem 3
#Urban Informatics

import sys
import numpy
import array
lines=sys.argv[3]
newlines = lines.split('\\n')

n=int(sys.argv[1])
m=int(sys.argv[2])

array=numpy.zeros((n,m))

for i in xrange(0,n):
	currentline=newlines[i]
	for j in xrange(0,m):
		currentspot=currentline[j]
		if currentspot=='*':
			if i==0:
				array[i+1,j]+=1
				if j!=0:
					array[i,j-1]+=1
					array[i+1,j-1]+=1
				if j!=m-1:
					array[i,j+1]+=1
					array[i+1,j+1]+=1
			elif j==0:
				array[i,j+1]+=1
				if i!=0:
					array[i-1,j+1]+=1
					array[i-1,j]+=1
				if i!=n-1:
					array[i+1,j]+=1
					array[i+1,j+1]+=1
			elif i==n-1:
				array[i-1,j]+=1
				if j!=0:
					array[i-1,j-1]+=1
					array[i,j-1]+=1
				if j!=m-1:
					array[i-1,j+1]+=1
					array[i,j+1]+=1
			elif j==m-1:
				array[i,j-1]+=1
				if i!=0:
					array[i-1,j-1]+=1
					array[i-1,j]+=1
				if i!=n-1:
					array[i+1,j-1]+=1
					array[i+1,j]+=1	
			else:
				array[i-1,j-1]+=1
				array[i-1,j]+=1
				array[i-1,j+1]+=1
				array[i,j-1]+=1
				array[i,j+1]+=1
				array[i+1,j-1]+=1
				array[i+1,j]+=1
				array[i+1,j+1]+=1

count=0

for i in xrange(0,n):
	currentline=newlines[i]
	count=0
	for j in xrange(0,m):
		currentspot=currentline[j]
		if currentspot=='*': 
			print "*",
		else: 
			print int(array[i,j]),
		count+=1
		if count==m:
			print ''
			


