import sys


def createField(givenField):
	output = givenField[1].split('\\n')
#	print output
	rows, cols = output[0].split()
	numRows=int(rows)
	numCols=int(cols)

	largeArr = []
	for x in range(1, numRows+1):
		#print x
		newArr = []
		charString =  output[x]
		for y in charString:
			#print y
			if (y=="."):
				y=0
			newArr.append(y)
			#print newArr
		largeArr.append(newArr)
	print largeArr
		 
	a = 0
	b = 1

	for a in range (0, len(largeArr)):
		for b in range (0, len(largeArr[a])):
			if (largeArr[a][b]=='*'):
				
				if (a+1<len(largeArr) and (b-1)>-1 and (largeArr[a+1][b-1])!='*'):
					(largeArr[a+1][b-1])+=1

				if (a+1<len(largeArr) and (largeArr[a+1][b])!='*'):
					(largeArr[a+1][b])+=1

				if ((a+1)<len(largeArr) and (b+1)<len(largeArr) and (largeArr[a+1][b+1])!='*'):
					(largeArr[a+1][b+1])+=1

				if (b+1<len(largeArr) and (largeArr[a][b+1])!='*'):
					(largeArr[a][b+1])+=1

				if ((b-1)>-1 and (largeArr[a][b-1])!='*'):
					(largeArr[a][b-1])+=1
				
				if ((a-1)>-1 and (b+1)<len(largeArr) and (largeArr[a-1][b+1])!='*'):
					(largeArr[a-1][b+1])+=1

				if ((a-1)>-1 and (largeArr[a-1][b])!='*'):
					(largeArr[a-1][b])+=1

				if ((b-1)>-1 and (a-1)>-1 and (largeArr[a-1][b-1])!='*'):
					(largeArr[a-1][b-1])+=1
	
	prettyprint(largeArr)

def prettyprint(arr):
	print "Field:"
	for item in arr:
  		print item[0],' '.join(map(str, item[1:]))

def main():
	givenField = sys.argv
	#print lines.split('\\n");
	createField(givenField)	


if __name__ == "__main__":
	main()
