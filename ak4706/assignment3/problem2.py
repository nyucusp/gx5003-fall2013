import sys
import csv
import numpy
from numpy import *
from StringIO import StringIO

txtfile = open('input2.txt','r')
input = txtfile.readlines()

#input = [elem.strip().split('\n') for elem in input]
print input

#number of case
cases = input[0][-2]
print cases

#loop through the cases
line = 0
loop = 0
while int(loop) < int(cases):
	#n = number of candidates
	n = int(input[2+line])
	print n

	#list of names
	names = input[3+line:int(3)+int(n)+line]
	print names

	#list of the ballots
	data = input[int(3)+int(n)+line:]
	print data
	ldata = len(data)
	print ldata

	#make a list count
	i = 0
	count=[]
	while i < n:
		count.append(0)
		i = i+ 1

	#count up the number of votes each candidate got
	r = 0
	c = 0
	while r < len(data):
		c = 0
		while c < n:
			if (int(data[r][0])-1 == c):
				count[c] = count[c] + 1
			c = c + 1
		r = r+1

	print 'count'
	print count

	#see if any of them got over half
	a =0
	num = sum(count) 
	print num
	half = float(num/2)


	while a < n:
		if count[a] > half:
			print names[a]
			sys.exit(0)
		else:
			a = a+1

	#if no one got over half then get the index of those who voted for the lowest
	minc=min(count)
	print minc
	minval = count.index(min(count))+1
	print "minval", minval

	print "data", data

	#make a list of just the first column
	r = 0
	col1=[]
	for num in data:
		if data[r][0]!='':
			col1.append(data[r][0])
			r = r+1

	#if the value in the column = the lowest voted candidate remove it
	#and put in the candidate that it voted for next
	print col1
	a=0
	while a < len(col1):
		if int(col1[a])==int(minval):
			print col1[a]
			col1.remove(col1[a])
			col1.append(data[a][2])
		a=a+1
	print col1

	#then count it up again
	i = 0
	count=[]
	while i < n:
		count.append(0)
		i = i+ 1

	r = 0
	c = 0
	while r < len(data):
		c = 0
		while c < n:
			if (int(col1[r])-1 == c):
				count[c] = count[c] + 1
			c = c + 1
		r = r+1

	print 'count'
	print count

	#and see if anyone got over half
	a =0
	num = sum(count) 
	print num
	half = float(num/2)


	while a < n:
		if count[a] > half:
			print names[a]
			sys.exit(0)
		else:
			a = a+1
	loop = loop +1
	line = int(4) + int(ldata) + int(n)
	# r=0
	# while r < len(col1):
	# 	int(data[r][0])=int(col1[r])
	# 	r = r+1
	# print data


# r = 0
# while r < len(data):
# 	if int(data[r][0])==int(minval):
# 		print data[r][0]
# 		data.remove(int(data[r][0]))
# 	r=r+1
# print data

# r=0
# b=0
# d=0
# while r<row:
# 	numpy.where((ndata[r][b]) == int(minval))
# 	r = r+1
# print ndata
# 		data.pop(int(ndata[r][b]))
# 		print int(data[r][b])
# 	r=r+1
# print data	

# count.remove(min(count))
# print count
# data = genfromtxt('input2a.txt', skip_header = 6)
# data = data.astype(int)
# print data
# row = 0
# for line in data:
# 	row = row + 1

# i = 0
# count=[]
# while i <=n:
# 	count.append(0)
# 	i = i+ 1

# r = 0
# c = 1
# while r < row:
# 	c = 0
# 	while c <= n:
# 		if (data[r,0] == c):
# 			count[c] = count[c] + 1
# 		c = c + 1
# 	for f in count:
# 		print count[f]
# 	print
# 	r = r+1
# while r < row:
# 	for num in count:
# 		print count[num]
# 	print
# 	count[data[r,0]] = count[data[r,0]] + 1
# 	#print count[data[r][0]]
# 	r = r+ 1

# for num in count:
# 	print count[num]