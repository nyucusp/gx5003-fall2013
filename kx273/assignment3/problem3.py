myFile=open("input3.txt","r") #open the input file
myInput=[]
index=0

for line in myFile: # read the file
    myInput.append(line.strip())
myFile.close()

while index<len(myInput):

    scenarioNum=int(myInput[index])
    paperNum=int(myInput[index+1].split(" ")[0])
    authorNum=int(myInput[index+1].split(" ")[1])

    authorList=[] #get the author list from the papers
    for i in range(index+2,index+2+paperNum):
        paper=myInput[i].split('.:')[0]
        authorList.append(paper.split('., '))

    for i in range(paperNum):# correct the authors' name by adding a "."
        for j in range(len(authorList[i])):
            authorList[i][j]=authorList[i][j]+"."

    authorErNum={} #creat a dictionary to store the authors and Erdos number
    for i in range(paperNum):
        for j in range(len(authorList[i])):
            if authorList[i][j] not in authorErNum and authorList[i][j]!='Erdos, P.':
                authorErNum[authorList[i][j]]=float('inf')

    for i in range(paperNum):#identiy authors whose Erdos number equal to 1 
        if 'Erdos, P.' in authorList[i]:
            for j in range(len(authorList[i])):
                if authorList[i][j]!='Erdos, P.':
                    authorErNum[authorList[i][j]]=1

    keepRunning=True
    ErNum=1
    while keepRunning:
        keepRunning=False
        authorTemp=[]

        for author in authorErNum: # get the author list whose Erdos number=ErNum
            if authorErNum[author]==ErNum:
                authorTemp.append(author)

        for i in range(paperNum):
            if bool(set(authorList[i])&set(authorTemp)): #check if contains the authors whose Erdos number=ErNum
                for j in range (len(authorList[i])):
                    if authorList[i][j]!='Erdos, P.' and authorErNum[authorList[i][j]]>ErNum+1:
                        authorErNum[authorList[i][j]]=ErNum+1
                        keepRunning=True #if certain Erdos number get updated, keep running the program

        ErNum+=1

    print ("Scenario"+" "+str(scenarioNum)) #output results
    for i in range(index+paperNum+2,index+paperNum+authorNum+2):
        authorCheck=str(myInput[i].strip())

        if authorCheck in authorErNum:
            if authorErNum[authorCheck]!=float('inf'):
                print (authorCheck+" "+ str(authorErNum[authorCheck]))
            else:
                print (authorCheck+" "+ "infinity")

    index=index+2+paperNum+authorNum #go to the next scenario

