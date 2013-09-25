import sys
from datetime import datetime

deadline = datetime.strptime(sys.argv[1],"%m/%d/%Y %H:%M:%S") #extract time from the input
myFile = open('logAfterAssignment1.txt','r') #open the log file
numbOfCommit=0
commit = [] 

for line in myFile:
     indexOfcommit = line.find("commit ")
     if(indexOfcommit != -1): #found the keyword "commit" from the line
          numbOfCommit+=1
     if(numbOfCommit==1): #store all the info from a commit
          commit.append(line)
     elif(numbOfCommit==2): #come to the end of a commit
          for term in commit:
               indexOfDate = term.find("Date:")
               if(indexOfDate != -1):#found date from the previous commit
                    commitTime=datetime.strptime(term[8:-7],"%a %b %d %H:%M:%S %Y")
          if(commitTime>deadline): #print commit later than the deadline
               for term in commit:
                    print term,

          commit=[]
          commit.append(line)
          numbOfCommit=1

myFile.close()


