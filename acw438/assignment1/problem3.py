#Alex Chohlas-Wood (acw438). Assignment 1, Problem 3.

import sys
raw = sys.argv[1]
raw = raw.split('\\n')

index = 0
fieldIndx = 0
output = list()
fieldNames = list()

while int(raw[index][0])!=0: #runs down "fields" until hits the last 0
    #get number of rows and column for field:
    numRows = int(raw[index][0]) 
    numCols = int(raw[index][2])

    #Setting up blank table of zeros:
    output.append([])
    for x in range(numRows):
        output[fieldIndx].append([])
        for y in range(numCols):
            output[fieldIndx][x].append(0)


    #Mining for mines:
    for x in range(numRows):
        for y in range(numCols):
            if raw[index+x+1][y] == "*":
                output[fieldIndx][x][y] = "*"
                #This increments all surrounding fields by 1
                for a in range(x-1,x+2):
                    for b in range(y-1,y+2):
                        if a >=0 and b>=0: #prevents field wraparound
                            #prevents error when incrementing another mine
                            try: 
                                output[fieldIndx][a][b] += 1
                            except:
                                pass

    index += numRows+1 #moves index to next field description
    fieldIndx += 1
    fieldNames.append("Field #" + str(fieldIndx) + ":")

for x in range(len(fieldNames)):
    print fieldNames[x]
    for y in output[x]:
        print ''.join(str(n) for n in y)
    print ""
