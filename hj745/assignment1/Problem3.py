row = int(input("row : "))
col = int(input("col : "))
fieldNum=1

while row and int :
    mm = [[0 for col in range(col)] for row in range(row)]  
    for i in range(row) :
        tmp = input('')
        for j in range(col) :
            if tmp[j]=='*' :
                mm[i][j]='*'
                for i2 in range(i-1, i+2) :
                    for j2 in range(j-1, j+2) :
                        if ((0<=i2) and (i2<row) and (0<=j2) and (j2<col) and (mm[i2][j2]!='*')) :
                            mm[i2][j2] = mm[i2][j2]+1
    print('Field #', fieldNum)
    
    for i in range(row):
        print(mm[i]) 
    row = int(input("row : "))
    col = int(input("col : "))
    fieldNum = fieldNum + 1