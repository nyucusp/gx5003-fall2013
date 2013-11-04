import csv
import sys
from decimal import *

#Open the input file and read it
txtfile = open('input1.txt', 'r')
input = txtfile.readlines()
#print input

#loop through the data if it's not = 0
loop = 0
while int(input[loop]) !=0:
	#count = 0
	# n = number of students
	n = input[loop]
	nloop = loop #copied the loop value so that I could keep the place so it would work the second time
	#count = count + 1
	#print n

# adding up the total amount for the trip
	i = 1
	sum=0
	#count = 0
	while i <= int(n):
		sum = float(input[int(nloop)+int(1)]) + float(sum)
		#count = count + 1
		i = i + 1
		nloop = nloop + 1
		#print sum
	#print sum

# evaluating cost per student and round so that it would give the least amount of change
	costps = float(sum)/float(n)
	costps = round(costps,2)
	#print costps

# if the student paid less than the cost per student than that money must be
#transferred to someone else, so it is added to the change
	i= 1
	change = 0
	while i <= int(n):
		if float(input[int(loop)+int(1)]) < costps:
			change = float(change) + (float(costps) - float(input[loop+1]))
		#print change
		i = i + 1
		loop=loop+1
	#print change
	print "$" + '%.2f' % change
	#setting the value for loop so it starts again unless it hit 0
	loop = int(loop)+int(1)