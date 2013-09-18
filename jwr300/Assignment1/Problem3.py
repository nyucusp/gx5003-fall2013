import sys

def main(argv):
	
	#print sys.argv[1]
	lines = sys.argv[1]
	global M
	M = int(lines[0][0])
	print M #development tracker for rows
	global N
	N = int(lines[2][0])
	print N #development tracker for columns

	inputList = lines.split('\\n')
	print inputList

	mineDict = createDict(inputList) #create mine dictionary
	print mineDict
	trackerDict =  createTrackerDict(mineDict) #create tracker dictionary
	print trackerDict

	field = mineDisplay(mineDict, trackerDict)
	print field

	mineOutput(mineDict)


#iterate through each cell and return mineCount
def createTrackerDict(mineDict):
	trackerDict = {}
	for k,v in mineDict.items(): # iterates through dictionary
		trackerDict[k[0],k[1]] = mineCount(mineDict,k[0],k[1]) #assigns minecount value for each cell in field
	return trackerDict

#pass the multi-input single array into a dictionary with key value pair as index

def createDict(inputList):
	i = 1
	values = []
	keys = []
	while i < (M+1):
		j = 0
		while j < N:
			print inputList[i][j]
			values.append(inputList[i][j])
			print i,j
			keys.append((i,j))
			j = j + 1
		i = i + 1
		print keys
		print values

	#build dictionary using dict function
	dictionary = dict(zip(keys, values))

	print dictionary
	return dictionary

def mineCount(mineDict, row, col):
    rowLength = M
    columnLength = N
    mineCount = 0
    for i in range(max(1,row-1),min(rowLength,row+2)):
        for j in range(max(0,col-1), min(columnLength,col+2)):
            if (i == row and j == col): #dont count the refence cell
                continue
            elif (mineDict[i,j] == "*"):
                mineCount += 1
    
    return mineCount


def mineDisplay(mineDict, trackerDict): 
	for k,v in mineDict.items():
		if mineDict[k[0],k[1]] != "*":
			mineDict[k[0],k[1]] = trackerDict[k[0],k[1]]

def mineOutput(mineDict):
	print "Field:", "\n"
	i = 1
	while i < (M+1):
	    j = 0
	    while j < N:
	        print mineDict[i,j],
	        j = j + 1
	    print "\n"
	    i = i + 1



if __name__ == "__main__":
	main(sys.argv)
