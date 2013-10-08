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
		
#the calculation part hasn't been finished
def getposition_up(griddata,worddata):
	if len(griddata)[0:i+1]>=wordlen:
		j=j-1
	else:
		getpostion_up(griddata,worddata)

def getposition_left(griddata,worddata):
	if len(griddata)[0:j+1]>=wordlen:
		j=j-1
	else:
		getpostion_up(griddata,worddata)

def getposition_right(griddata,worddata):
	for k in worddata:
		wordlen=int(len(worddata[i]))#get the length of each word
		for i in range (0,m):
			for j in range(0,n):
				for g in range(0,wordlen+1):
					while griddata[i][j]==worddata[k][0]:
						if len(griddata[j:])>=wordlen:
							j=j+1
						else:
							getposition_left(griddata,worddata)
						return
						






def eachcasedata(eachcase):
	m=int(allcasedata[0].split()[0])#number of lines in the grid
	n=int(allcasedata[i].split()[1])#number of columes in the grid
	grid=[m,n]

	griddata=[]
	griddata.append(allcasedata[1:m+1])#put the data of grid into an array

	w=int(allcasedata[m+1])#number of words that could be found in the grid
	worddata=[]
	worddata.append(allcasedata[m+2:m+2+w])#put the words into an array
	
	getposition(griddata,worddata)
	return	




allcasedata=[]#find the data of every case and put them into a new array
for b in range(0,len(blankposition)-1):
	x=blankposition[b]+1#the case content starts from the next line of the first space
	y=blankposition[b+1]#the case content ends in the line before the space
	allcasedata.append(readdata[x:y])
	for eachcase in allcasedata:
		
		eachcasedata(eachcase)
