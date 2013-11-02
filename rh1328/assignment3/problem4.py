#blank lines between each separate case 


def wordSearch(theBoard, wordsToFind, r, c):
	temp = 0
	for word in wordsToFind:
		boardIndex = 0
#will use the check functions to increment through the rest of the word 
		letter = word[temp]
		while boardIndex < r:		
			if theBoard[boardIndex].find(letter) != -1:
				wordIndex = 0
				checkBool = False
				firstLetterIndex = theBoard[boardIndex].find(letter)
				#print "letter found at" + str(boardIndex) + str(firstLetterIndex)
				checkBool = checkHorizontal(firstLetterIndex-1, word, boardIndex, theBoard, wordIndex)
				if checkBool:
					print boardIndex, firstLetterIndex
					boardIndex = r
					temp += 1
					continue
				else:
					boardIndex +=1	
			else: 
				boardIndex+=1


def checkHorizontal(letterIndex, word, boardIndex, theBoard, wordIndex):
#increment through line in board horizontally while incrementing through word to find to see if
#the entire word is present in that line, if not return to wordSearch and continue
#searching through board
	toReturn = False
	strToCheck = theBoard[boardIndex]
	if word[wordIndex] != '\n':
		if strToCheck[letterIndex+1] != -1:		
		#	print "string containing the letter" + "l"+strToCheck[letterIndex+1]+"l"
		#	print "character in word checking to" + "l"+word[wordIndex]+"l"
			if strToCheck[letterIndex+1] == word[wordIndex]:
				return checkHorizontal(letterIndex+1, word, boardIndex, theBoard, wordIndex+1)
			else:
				return toReturn
		elif strToCheck[letterIndex+1] != -1:
			return toReturn
	elif word[wordIndex] == '\n':	
		toReturn = True
		#print "i'm returning"
		return toReturn 


def scenarios(lines, numCases, x):
#structre separate arrays for different scenarios and organize information
	if x < numCases:
		#get rid of preceding white space before new board dimensions
		#parse rows and cols
		del lines[0]
		r,c = lines[0].split()
		r = int(r.strip())
		c = int(c.strip())
		del lines[0]
		
		#make arr for wordsearch
		arr = []
		while x < r:
			arr.append(lines[0])
			x += 1
			del lines[0]
	
		#make all letters lowercase:
		arr = [item.lower() for item in arr]
	#	print arr

#figure out number/what words to look for and append to array	
		numWords = lines[0]
		numWords = numWords.strip()
		numWords = numWords.rstrip("\n")
		numWords = int(numWords)
		del lines[0]
		y = 0
		wordsToFind = []
		while y < numWords:
			wordsToFind.append(lines[0])
			y = y+1
			del lines[0]
		wordsToFind = [thing.lower() for thing in wordsToFind]
#		print wordsToFind
		wordSearch(arr, wordsToFind, r, c)
		scenarios(lines, numCases, x+1)


	
def main():
	with open("input4.txt", "r") as thefile:
		lines = thefile.readlines()
	numCases = lines[0]
	numCases = numCases.strip()
	numCases = numCases.rstrip("\n")
	numCases = int(numCases)
	x = 0
	del lines[0]
	scenarios(lines, numCases, x) 


if __name__ == "__main__":
	main()
