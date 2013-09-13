# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:12:34 2013
@author: yz1897
"""
import sys

def Neighbors(n,m,i):
    nb=[]
    #up
    if i>m:
        nb.append(i-m)
        #up left
        if i%m>0:
            nb.append(i-m-1)
        #up right
        if i%m<m-1:
            nb.append(i-m+1)
    #below
    if i/m<n-1:
        nb.append(i+m)
        #below left
        if i%m>0:
            nb.append(i+m-1)
        #below right
        if i%m<m-1:
            nb.append(i+m+1)
    #left
    if i%m>0:
        nb.append(i-1)
    #right
    if i%m<m-1:
        nb.append(i+1)
    return nb
    
    
def Note_Mine(n,m,mmap):
    total=n*m
    
    safe=0#to deside which strategy to use
    tagmap=range(total)#to record the result map
    for i in range(total):
        if mmap[i]=="*":
            tagmap[i]="*"
        else:
            safe+=1
            tagmap[i]=0
            
    if safe<total/2:#Tag by safesquare '.'
        for i in range(total):
            if mmap[i]=='.':
                nblist=Neighbors(n,m,i)
                for nb in nblist:
                    if mmap[nb]=="*":
                        tagmap[i]+=1
    else:#Tag by mine
        for i in range(total):
            if mmap[i]=="*":
                nblist=Neighbors(n,m,i)
                for nb in nblist:
                    if mmap[nb]!="*":
                        tagmap[nb]+=1
    for i in range(n):
        line=''
        for j in range(m*i,m*(i+1)):
            line+=str(tagmap[j])
        print line
        
if __name__ == "__main__":
    Note_Mine(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
    #Note_Mine(3,4,"*..*.....*..")
    
