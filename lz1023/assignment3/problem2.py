
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


def find_winner(allcasedata):
	for i in allcasedata:#handle the data in every case
		candidatenum=int(i[0])#get the number of candidates and let it be an integer
		name=i[1:candidatenum+1]#get the candidates'name and put them into an array
		votedata=i[candidatenum+1:len(i)]#get the votes and put them into an array

		vote={}#create a dic, make the number(such as No.1, No.2) as keys and 
		#count the votes of each number as values of the dic

		for j in votedata:
			votenum=len(votedata)#get the number of how many votes there are
			voteline=votedata[j].split()#split the data on a vote
			firstvote=int(voteline[0])#get the first choice on a vote
			if firstvote not in vote:#add the number of first choice as keys
				vote[firstvote]=1#and calulate how many votes that each number got as values
			else:
				vote[firstvote]+=1

		vote_value=[]#get the winner whose votes are more than 50%
		for n in vote:
			vote_value.append(vote[n])
			percent=vote[n]/votenum	
			if percent>0.5:
				winner=name[n-1]
				print winner
				return

			if max(vote_value[n])==min(vote_value[n]):#tie
				for n in vote:
					print name[n-1]
				return

		    if max(vote_value[n])<=0.5, n>2:#delete the candidate who got the least votes
		    	
		    	del 
		    # I can't figure out this part


allcasedata=[]#find the data of every case and put them into a new array
for b in range(0,len(blankposition)-1):
	x=blankposition[b]+1#the case content starts from the next line of the first space
	y=blankposition[b+1]#the case content ends in the line before the space
	allcasedata.append(readdata[x:y])
	find_winner(allcasedata)
		


	



	


