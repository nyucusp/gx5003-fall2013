import sys
line=sys.argv[1]
line=line.split('\\n')
index=0
fldnum=1 #Denote the number of the field

while index<len(line):
    rownum=int(line[index][0]) #get the number of rows for field
    colnum=int(line[index][2]) #get the number of columns for field

    if rownum>0 and colnum>0:
        print "Field #"+str(fldnum)+":"
        for i in range(index+1, rownum+index+1):
            result="" #use a string variable to output the result
            for j in range(colnum):
               if line[i][j]=="*":
                   result=result+"*"
               else:
                   count=0 # store the number of adjcent mines
                   for m in range(i-1,i+2):
                       for n in range(j-1,j+2):
                           if m>=0 and m<=rownum+index and n>=0 and n<colnum: #define the valid index 
                              try:
                                  if line[m][n]=="*":
                                      count=count+1
                              except:
                                  pass
                   result=result+str(count)
            print result
        print "\n"
    else:
        break

    index=index+rownum+1
    fldnum=fldnum+1






