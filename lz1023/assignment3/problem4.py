myFile=open('input4.txt','r')#read the input file and put all data into an array
readdata=[]
for line in myFile:
	readdata.append(line[:-1])
myFile.close

readdata.append('')#add a space into the end of array to indicate the last case ends

blankposition=[]#find the space position in the readdata and put them into another array
for a in range(1,len(readdata)):
	if readdata[a]=='':
		blankposition.append(a)
casenumber=int(readdata[0])#get the number of how many cases there are		

#Here I wanna define a function to calculate the position where each word appears 
#in the grid. I will get the first letter of the first word to find the position
#where has the same letter. Then I will check whether the left lenths in 8 directions
#are longer than the word's lenth. If longer, check whether the next (lengh-1) letters
#are the same as the word's left (lenth-1) letters. If they are matched, I can get the
#position and then loop this calculating process for all words.

#I have tried my best but writing the code of this process is too complicated for me.

def get_position():
	
	for i in range(0,casenumber):
		eachworddata=worddata[i]
		for j in (0,len(worddata[i])):
			word=eachworddata[i][j]
			firstletter=word.split()[0]#get the first letter of the word
			for k in range(0,casenumber):
				if firstletter in griddata[k]:




griddata=[]
worddata=[]
def eachcase():
	allcasedata=[]#find all case data and put them into a new array
	for b in range(0,len(blankposition)-1):
		x=blankposition[b]+1#the case content starts from the next line of the first space
		y=blankposition[b+1]#the case content ends in the line before the space
		allcasedata.append(readdata[x:y])
	


		
	for i in range(len(allcasedata)):#get the data of each case 
		eachcasedata=[]
		eachcasedata=allcasedata[i]

		m=int(eachcasedata[0].split()[0])#number of lines in the grid
		n=int(eachcasedata[0].split()[1])#number of columes in the grid
				

		
		griddata.append(eachcasedata[1:m+1])#put the data of grid into an array

		w=int(eachcasedata[m+1])#number of words that could be found in the grid
		
		worddata.append(eachcasedata[m+2:m+2+w])#put the words into an array
		
		
eachcase()
	
		






