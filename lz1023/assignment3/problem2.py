
myFile=open('input2.txt','r')#read the input file and put all data into an array
readdata=[]
for line in myFile:
	readdata.append(line[:-1])
myFile.close



readdata.append('')#add a space into the end of array to indicate the last case ends

blankposition=[]#find the space position in the readdata and put them into another array
for a in range(1,len(readdata)):
	if readdata[a]=='':
		blankposition.append(a)

def winner(name,votedata):
	result=False

	vote={}#create a dic, make the number(such as No.1, No.2) as keys and 
	#count the votes of each number as values of the dic

	for i in votedata:
		votenum=len(votedata)#get the number of how many lines of votes there are
		voteline=votedata[i]
		for j in votedata:
			firstvote=int(voteline[j][0].split())#split the data of a line and get the first choice on a vote
			if firstvote not in vote:#add the number of first choice as keys
				vote[firstvote]=1#and calulate how many votes that each number got as values
			else:
				vote[firstvote]+=1

	vote_value=[]#get the winner whose votes are more than 50%
	for n in vote:
		vote_value.append(vote[n])
		percent=vote[n]/votenum	
		if percent>0.5:
			result=True
			winner=name[n-1]
			print winner
			return

		if max(vote_value[n])==min(vote_value[n]) and len(vote_value)>1:#get the result in the condition of tie
			result=True
			for n in vote:
				print name[n-1]
				return

		
		#delete the candidate who got the least votes
		if result==False:	
			new_votes=[]	
			deletename=[]
			loser=min(vote_value[n])
		for k in vote:
			if vote[k]==min(vote_value[n]):
				deletename.append(k)#if k isn't in new_votes, put it into an array to delete the looser
		
		for n in range(len(votedata)):
			new_votes.append([])
			for k in votedata[n]:
				if int(k) not in deletename:
					new_votes[n].append(k)    	
		winner(name,votedata)
		  
name=[]
votedata=[]
def eachcase():

	allcasedata=[]#find the data of every case and put them into a new array
	for b in range(0,len(blankposition)-1):
		x=blankposition[b]+1#the case content starts from the next line of the first space
		y=blankposition[b+1]#the case content ends in the line before the space
		allcasedata.append(readdata[x:y])

	for i in range(len(allcasedata)):#get the data of each case 
		eachcasedata=[]
		eachcasedata=allcasedata[i]	
			
		
		candidatenum=int(eachcasedata[0])#get the number of candidates and let it be an integer
		name.append(eachcasedata[1:candidatenum+1])#get the candidates'name and put them into an array
		votedata.append(eachcasedata[candidatenum+1:len(eachcasedata)])#get the votes and put them into an array
		
		winner(name,votedata)

eachcase()


	


