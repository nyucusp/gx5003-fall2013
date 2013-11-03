myFile=open('input4.txt','r')#read the input file and put all data into an array
readdata=[]
for line in myFile:
	line_lower=line.lower()#change the letters of the data to lowercase 
	readdata.append(line_lower[:-1])
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



#This part hasn't been finished.

def directions(eachgriddata,eachworddata,x,y,j):
	for i in range(1,len(eachworddata[i])):#check whether the left length 
	#in each direction is not smaller than the word's length
		wordlen=int(eachworddata[i])
		if len(eachgriddata[0])-y>=wordlen:#right
			for i in range (1,len(eachworddata[j])):
			while eachgriddata[x][y+1] == eachworddata[j][i]:
				y=y+1
				if y-len(eachworddata[j])>

		if y+1>=wordlen:#left
			
		if len(eachgriddata)-x>=wordlen:#down
			

		if x+1>=wordlen:#up
			

		if 	
#This part hasn't been finished.



def get_position(eachgriddata,firstletter,j):
	for x in range(0,len(eachgriddata)):#find the position of first letter in the grid
		for y in range(0,len(eachgriddata[0])):
			if eachgriddata[x][y]==firstletter:
				directions(eachgriddata,eachworddata,x,y,j)
#This part hasn't been finished.				



for i in range(0,casenumber):#get everycase's grid and word data, and the first letter of each word
	eachworddata=worddata[i]
	eachgriddata=griddata[i]
	for j in range(0,len(eachworddata)):
		firstletter=eachworddata[j][0]
		
		get_position(eachgriddata,firstletter,j)
	






