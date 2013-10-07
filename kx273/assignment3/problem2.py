myFile=open("input2.txt","r") #open the input file
myInput=[]
index=0

for line in myFile: # read the file
    myInput.append(line.strip())
myFile.close()

while index<len(myInput):
    
    scenarioNum=int(myInput[index])
    candidNum=int(myInput[index+2])
    candidDict={} #define a dictionary for candidates
    for i in range(candidNum):
        name=myInput[index+3+i]
        candidDict[i+1]={'name':name,'votenum':0,'voteindex':[],'status':0} 
    

    ballot=[]
    for i in range(index+3+candidNum,len(myInput)): #read the ballots
        if myInput[i]!="":
            ballot.append(myInput[i].split(" "))
        else:
            break
    ballotNum=len(ballot)

    teminate=False
    initialCheck=0
    while teminate==False: #keep running until one candidate receive more than 50% votes.

        if initialCheck==0: #initialize the ballot info
            for i in range(ballotNum):
                candidID=int(ballot[i][0])#read the candidID from each ballot
                candidDict[candidID]['votenum']+=1
                candidDict[candidID]['voteindex'].append(i)
        initialCheck=1 

        ballotNumSum=0
        candidActNum=0
        ballotNumMin=ballotNum
        ballotNumMax=0
        for i in candidDict: #get the minumum, maximum, sum of ballot number and active candidates number
            if candidDict[i]['status']==0:
                ballotNumSum+=candidDict[i]['votenum']
                candidActNum+=1

                if candidDict[i]['votenum']<ballotNumMin:
                    ballotNumMin=candidDict[i]['votenum']

                if candidDict[i]['votenum']>ballotNumMax:
                    ballotNumMax=candidDict[i]['votenum']

        if ballotNumMin==ballotNumMax and candidActNum>1: #all remaining candidates are tied
            teminate=True
            print"All remaining candidates are tied. "+''
                
        for i in candidDict:#if one candidate receive more than 50% vote, teminate the voting
            if candidDict[i]['status']==0:
                        
                if float(candidDict[i]['votenum'])/float(ballotNumSum)>0.5:
                    print candidDict[i]['name']+'\n'   
                    teminate=True


        recountList=[]
        for i in candidDict: #get the index of ballot need to be recounted 
            if candidDict[i]['status']==0:
                if candidDict[i]['votenum']==ballotNumMin:
                    recountList+=candidDict[i]['voteindex']
                    candidDict[i]['status']=1 #eliminate the candidates with the minumum ballot number
       
        for recountIndex in recountList: #recount ballots
            try:
                ballot[recountIndex]=ballot[recountIndex][1:]
                candidID=int(ballot[recountIndex][0])
                candidDict[candidID]['votenum']+=1
                candidDict[candidID]['voteindex'].append(recountIndex)
            except:
                pass

    index=index+4+candidNum+ballotNum #move to the next scenario




