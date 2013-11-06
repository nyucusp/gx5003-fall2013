f = open ("input1.txt","r")

fileLines = f.readlines()
numberOfLines = len(fileLines)
lineIndex = 0

while(lineIndex < numberOfLines):
	numberOfStudents = int(fileLines[lineIndex])
	if(numberOfStudents == 0):
		break
	lineIndex = lineIndex + 1
	costs = []
	for t in range(0,numberOfStudents):
		costs.append(float(fileLines[lineIndex]))
		lineIndex = lineIndex + 1


	sumCosts = 0
	for cost in costs:
		sumCosts = sumCosts + cost
	

	averageCost = sumCosts / numberOfStudents

	sumOfPostives = 0
	for cost in costs:
		differeceCost = averageCost - cost
		differeceCost = int(100*differeceCost)/100.0
		if(differeceCost > 0):
			sumOfPostives = sumOfPostives + differeceCost
	print "$" + str(sumOfPostives)
