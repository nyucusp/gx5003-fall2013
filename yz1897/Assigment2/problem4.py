# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:19:54 2013

@author: yilong
"""

#from borough import *
from borough import Borough

#reuse the functions in problem 4
from problem3 import getzippopulation,getboroughzipcode

from sys import argv as bname


if __name__=="__main__":
    #get the population and borough information from the data in dictionary form
    populationdic=getzippopulation()
    boroughdic=getboroughzipcode()
    
    #turn the input into the captalized form
    bname=bname[1].split(' ')[0].capitalize()

    #initialize the object in Borough class
    BOROUGH=Borough(bname)
    
    #put the data stored from two dictions into the object
    for zp in boroughdic[bname]:
        if zp in populationdic:
            BOROUGH.addZipcode(zp)
            BOROUGH.addPopulation(populationdic[zp])
    
    #use the class function to get the average number
    print BOROUGH.PopuPerZip()
    
                