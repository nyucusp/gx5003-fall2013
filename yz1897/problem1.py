[[C# -*- coding: utf-8 -*-

"""
Created on Thu Sep 12 15:18:57 2013
Net ID yz1897
@author: yilong
"""

# input function
def inputdata():
    inputline=raw_input()
    i,j=inputline.split(' ')
    return int(i),int(j)


# basic solution:
def Solution1(n):
    count=1
    while True:
        if n==1:            
            return count
        else:
            count+=1
            if n%2==0:
                n=n/2
            else:
                n=n*3+1

# controling for basic solution
print "Testing the basic solution\nPlease input:"
while True:    
    try:         
        i,j=inputdata()
    except:
        print 'Error, input again'
        break
    result_list=[Solution1(n) for n in range(min(i,j),max(i,j)+1)]
    print i,j,max(result_list)
