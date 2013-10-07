
myFile = open('input1.txt','r') #open the input file
myInput=[]
index=0


for line in myFile:# read the file
    myInput.append(line.strip())
myFile.close()

while index<len(myInput):
    if int(myInput[index])!=0:#terminate it when meet 0
        studentNum=int(myInput[index])
        if studentNum<=1000:
            cumCost=0
            for i in range(index+1,index+studentNum+1):
                cost=float(myInput[i])
                if cost<=10000:
                    cumCost+=cost
                else:
                    print ("Cost for each student should be no more than 10,000$")
                    break
            
            avgCost= round(cumCost/studentNum,2) #minimum amount of money is one cent
            changeHand=0.0
            for i in range(index+1,index+studentNum+1): #get the amount of money that must change hands
                if float(myInput[i])<avgCost:
                    changeHand+=(avgCost-float(myInput[i]))
                    changeHand=round(changeHand,2)

            if avgCost>0:
                print("&"+str(changeHand))   

        else:
            print ("The student number should be no more than 1000")
            break  
        
        index=index+studentNum+1 #move to the next trip
    else:
        break

