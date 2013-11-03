import sys
from DateTime import DateTime

deadline = DateTime.strptime(sys.argv[1],"%m/%d/%Y %H:%M:%S") 
myFile = open('logAfterAssignment1.txt','r') 
numbOfCommit=0
commit = [] 

for line in myFile:
     indexOfcommit = line.find("commit ")
     if(indexOfcommit != -1): 
          numbOfCommit+=1
     if(numbOfCommit==1): 
          commit.append(line)
     elif(numbOfCommit==2): 
          for term in commit:
               indexOfDate = term.find("Date:")
               if(indexOfDate != -1):
                    commitTime=DateTime.strptime(term[8:-7],"%a %b %d %H:%M:%S %Y")
          if(commitTime>deadline): 
               for term in commit:
                    print term,

          commit=[]
          commit.append(line)
          numbOfCommit=1

myFile.close()


