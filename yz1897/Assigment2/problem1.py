# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:32:28 2013

@author: yilong
"""

import time
import sys


def find_late_student():
    try:
        deadline=sys.argv()[1]
        #get the deadline as parameter
    except:
        deadline='09/19/2013 09:12:15'#
    find=0
    for line in file("c:/works/dropbox/Git/data/logsofar.txt"):
        #record the author information, update every time reading a new log
    
        if line.find("Author:")!=-1:
            Author=line[:-1].split(": ")[1]
    
        if line.find("Author:")!=-1:
            Author=line[:-1].split(": ")[1]
            
        #record the data information
        find=line.find("Date:")
        if find!=-1:
            committime=line[:-1].split(":   ")[1]
            time1=time.strptime(committime[:-6],"%a %b %d %H:%M:%S %Y")
            time2=time.strptime(deadline,"%m/%d/%Y %H:%M:%S")
            if time2<time1:
                print Author
                print time1
                
if __name__=="__main__":
    find_late_student()            