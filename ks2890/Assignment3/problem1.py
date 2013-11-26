from decimal import Decimal

f = open('input1.txt', 'r')
fileLines = f.readlines()
numberOfLines = len(fileLines)
lineIndex = 0

while(lineIndex < numberOfLines):
	num_array = list()
	num = fileLines[lineIndex]
	lineIndex = lineIndex + 1
	num = int(num)
	if(num == 0):
		break
	answer = 0

	for i in range(0,num):
		line = fileLines[lineIndex]
		lineIndex = lineIndex + 1
		num_array.append(float(line))

	#print num_array

	sumOfnum = sum(num_array)
	avgOfnum = sumOfnum/num
	#print avgOfnum

	for i in range(0,num):
		if num_array[i]-avgOfnum >0:
			answer = answer + (num_array[i]-avgOfnum)
			#print (num_array[i]-avgOfnum)
	print answer

