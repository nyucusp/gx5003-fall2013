# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 16:16:09 2013

@author: yilong
"""

class Borough:
    name=None
    zipcodes=None
    population=None
    def __init__(self, name):#initialize
        self.name=name
        self.zipcodes=[]
        self.population=0
        
    def addZipcode(self,zp):#
        self.zipcodes.append(zp)
        
    def addPopulation(self,p):
        self.population+=p
        
    def PopuPerZip(self):
        return float(self.population)/len(self.zipcodes)

