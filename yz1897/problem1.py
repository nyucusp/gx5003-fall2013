# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:18:57 2013
@author: yz1897
"""
import sys

# this solution should be faster in c, but in after i test
#in python, the it get a little slower...
def Longest_Cycle(i,j):
    longest=0        
    deleted=[-1 for k in range(j-i+1)]

    for n in range(j,i-1,-1):
        if deleted[n-i]==1:
            continue
        deleted[n-i]=1
        count=1
        while True:
            if n==1:
                break
            #mark appeared number
            if n>=i and n<j and deleted[n-i]==-1:
                deleted[n-i]=1
            count+=1
            if n%2==0:
                n=n/2
            else:
                n=n*3+1
        if longest<count:
            longest=count
    print i,j,longest

if __name__ == "__main__":
    Longest_Cycle(int(sys.argv[1]),int(sys.argv[2]))
