
import sys
import numbers 
import os 
import ast 

inputFile = open('input1.txt','r') 
inputLine = inputFile.readlines()

## Clean the Data ## 
inputClean = []
for x in inputLine:
	x =	x.rstrip(os.linesep)
	inputClean.append(x) 

## Created a List of Input ## 
inputNumeral = []
for x in inputClean:
	inputNumeral.append(ast.literal_eval(x))

for x in inputNumeral:
	if x != 0: ## Identified if it is the last information for the last trip ## 
		if isinstance(x,int): ## Identified if it is a single integer denoting teh number of students ##  
			sumlist =[]
			finallist = []
			n = x ## Identified the Number of Students ##
			count = 1 
			position = inputNumeral.index(x)
	
			while count <= n: 
				sumlist.append(inputNumeral[(position + count)]) 
				count = count + 1
				average = int(sum(sumlist)/n) ##  Found each student's share ## 

			for x in sumlist:
				if (x - average) < 0: 
					finallist.append(-(x - average)) ## Found How much money needs to be exchanged ## 

			print'$' + ("%.2f" % sum(finallist))

inputFile.close  