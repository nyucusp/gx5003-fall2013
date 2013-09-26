datas = []
outputs = []
    
        
#count how many mines
def check(val,m,n,datas,lines,columns):
    
    if val=='*':
        return '*'
    else:
        num1 = isMine(m-1,n-1,datas,lines,columns)
        num2 = isMine(m-1,n,datas,lines,columns)
        num3 = isMine(m-1,n+1,datas,lines,columns)
        num4 = isMine(m,n-1,datas,lines,columns)
        num5 = isMine(m,n+1,datas,lines,columns)
        num6 = isMine(m+1,n-1,datas,lines,columns)
        num7 = isMine(m+1,n,datas,lines,columns)
        num8 = isMine(m+1,n+1,datas,lines,columns)
        return num1+num2+num3+num4+num5+num6+num7+num8
    
        
def isMine(l,c,datas,lines,columns):
    #print str(l)+' hang ,'+ str(c)+'lie' + ',totle ' + str(lines) +'h ' + str(columns) + ' cols'
    if l<0 or c<0 or l>=lines or c>=columns:
        return 0
    else:
        
        v = datas[l][c]
        if v=='*':
            return 1
        else:
            return 0
            
def main():
    twoNumber = raw_input('please input 2 number:')
    nums = twoNumber.split(' ')
    if len(nums)!=2:
        print 'error input, please input 2 number'
    else:
        lines = int(nums[0])
        columns = int(nums[1])
        if lines>0 and lines<=100 and columns>0 and columns<=100:
            for i in range(lines):
                data = raw_input('please input chars denoted by . or *')
                if len(data)!=columns:
                    print 'error input'
                else:
                    datas.append(data)
                
            for m in range(lines): 
                perline = datas[m]
                output = ''
                for n in range(columns):
                    
                    res = check(perline[n],m,n,datas,lines,columns)
                    output += str(res)
                outputs.append(output)
            
            for m in range(lines):
                print outputs[m]
                
        else:
            print 'error input, the 2 numbers may be 0,100'
            
if __name__=="__main__":
    main()