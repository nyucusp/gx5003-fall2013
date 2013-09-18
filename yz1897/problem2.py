# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:12:38 2013
@author: yz1897
"""
import sys

def Judge_Jully(element):
    element=[int(i) for i in element]
    length=element[0]
    # main alg
    space=[-1 for i in range(length)]#Record whether a number have appeared
    for i in range(1,length):
        difference=abs(element[i]-element[i+1])
        if difference>=length or difference<1 or space[difference]==1:
            print "Not jolly"
            return
        else:
            space[difference]=1
    print "Jolly"

if __name__ == "__main__":
    Judge_Jully(sys.argv[1:])
