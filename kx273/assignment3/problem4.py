def find_location(string,matrix): # find the location of keyword 
    location=[float("inf"),float("inf")]
    lineNum=len(matrix)
    colNum=len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].lower()==string[0].lower():
                lStr=string[0].lower()
                rStr=string[0].lower()
                uStr=string[0].lower()
                dStr=string[0].lower()
                ulStr=string[0].lower()
                urStr=string[0].lower()
                dlStr=string[0].lower()
                drStr=string[0].lower()

                for n in range (1,len(string)): #get the string in eight horizontal, vertical and diagonal directions through the matrix
                    
                    if i in range(lineNum) and j-n in range(colNum):
                        lStr+=matrix[i][j-n]

                    if i in range(lineNum) and j+n in range(colNum):                    
                        rStr+=matrix[i][j+n]

                    if i-n in range(lineNum) and j in range(colNum):
                        uStr+=matrix[i-n][j]

                    if i+n in range(lineNum) and j in range(colNum):
                        dStr+=matrix[i+n][j]

                    if i-n in range(lineNum) and j-n in range(colNum):
                        ulStr+=matrix[i-n][j-n]

                    if i-n in range(lineNum) and j+n in range(colNum):
                        urStr+=matrix[i-n][j+n]

                    if i+n in range(lineNum) and j-n in range(colNum):
                        dlStr+=matrix[i+n][j-n]

                    if i+n in range(lineNum) and j+n in range(colNum):
                        drStr+=matrix[i+n][j+n]


                if lStr.lower()==string.lower() or rStr.lower()==string.lower() or uStr.lower()==string.lower() or dStr.lower()==string.lower() or ulStr.lower()==string.lower() or urStr.lower()==string.lower() or dlStr.lower()==string.lower() or drStr.lower()==string.lower():
                    location[0]=i+1
                    location[1]=j+1
                    return location
    return location
    
   

myFile=open("input4.txt","r") #open the input file
myInput=[]
index=0

for line in myFile: # read the file
    myInput.append(line.strip())
myFile.close()

while index<len(myInput):

    scenarioNum=int(myInput[index])
    lineNum=int(myInput[index+2].split(" ")[0])
    columnNum=int(myInput[index+2].split(" ")[1])
    checkNum=int(myInput[index+lineNum+3])

    matrix=[]
    for i in range(index+3,index+3+lineNum):
        matrix.append(myInput[i])
             
    for i in range(index+4+lineNum, index+4+lineNum+checkNum):
        location=find_location(myInput[i],matrix) #get the locations 
        print(str(location[0])+" "+str(location[1]))

    print ('')
    index=index+lineNum+checkNum+5 #move to the next scenario

