#Katherine Elliott
#Assignment 1 Problem 3

import sys

lines = sys.argv[1]

def readFile(inputval):
    m,n =inputval.readline.rstrip().split()
    m = int(m)
    n = int(n)
    field = []
    
    if me ==0 or n ==0:
        return None
        
    for i in range(m):
        line = list(sys.argv[1].readline().rstrip())
        field.append(line)
    
def check(coord):
    if coord == "*":
        return 1
    return 0

def processField(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            count = 0
            if field[i][j] == "*":
                continue
            if i == 0:
                count+= check(field[i+1][j])
            if j == 0:
                count+= check(field[i][j+1])
                count+= check(field[i+1][j+1])
            elif j == len(field[1])-1:
                count+= check(field[i][j-1])
                count+= check(field[i+1][j-1])
            else:
                count+= check(field[i][j-1])
                count+= check(field[i][j+1])
                count+= check(field[i+1][j-1])
                count+= check(field[i+1][j+1])
        elif i == len(field)-1:
            count+= check(field[i-1][j])
            if j == 0:
                count+= check(field[i][j+1])
                count+= check(field[i-1][j+1])
            elif j == len(field[i])-1:
                count+= check(field[i][j-1])
                count+= check(field[i-1][j-1])
            else:
                count+= check(field[i][j+1])
                count+= check(field[i-1][j+1])
                count+= check(field[i][j-1])
                count+= checkfield(field[i-1][j-1])        
        else:
            count+= check(field[i-1][j-1])
            count+= check(field[i+1][j])
            
            if j == 0 or j != len(field[i])-1:
                count+= check(field[i-1][j+1])
                count+= check(field[i][j+1])
                count+= check(field[i+1][j+1])
            if j == len(field)-1 or j !=0:
                count+= check(field[i-1][j-1])
                count+= check(field[i][j-1])
                count+= check(field[i+1][j-1])
                
        field [i][j] = count

    return field

def writeFile(field, ouput, numField)
    print >> output "Field %s" % numField:
    for line in field:
        for charac in line:
            output.writes(str(charac))
        print >> output
    print >> output
                    
            