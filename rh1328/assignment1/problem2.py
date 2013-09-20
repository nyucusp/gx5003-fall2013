import sys
import math

def jollyJumper(numArray):
	if (int(numArray[1]) > 3000 or int(numArray[1]) < 0):
		print "error"
		sys.exit(0)

	subtractArray = []
	num1 = 2
	num2 = 3 
	length = int(numArray[1]-1)

	while (num2 < len(numArray)):		
		result = math.fabs(int(numArray[num1]) - int(numArray[num2]))
		num2 += 1
		num1 += 1
		subtractArray.append(result)
	
	testNum = 1
	while (testNum < length):
		if testNum in subtractArray:
			testNum +=1
		else:
			print "Not Jolly"
			sys.exit(0)
	print "Jolly"


def main():
	numArr=sys.argv
	counter = 0
	for num in sys.argv[1:]:
		counter+=1
		try:
			numArr[counter] = int(num)
		except:
			print "error"
			sys.exit(0)

	jollyJumper(numArr)

if __name__ == "__main__":
	main()
