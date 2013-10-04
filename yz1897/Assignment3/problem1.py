# -*- coding: utf-8 -*-
"""
Created on Wed Oct 02 17:36:06 2013

@author: yilong
"""

import sys

def Mini_Exchange(costlist):
    costs=[float(i) for i in costlist]#get all the input in float
    total=sum(costs)
    average=total/len(costs)
    exchange=0#the amount of money to be exchange
    
    loweraverage=int(100*average)/100.0
    #in this method, use the lower interger will recuce the total exchanges
    for i in costs:
        if i<loweraverage:
            exchange+=loweraverage-i
    return exchange

def PrintAmount(Exchanges):#make the output into the required form
    for exchange in Exchanges:
        figures=str(exchange).split('.')
        digits=figures[1]
        if len(digits)==1:
            digits+='0'
        line='$'+figures[0]+'.'+digits
        print line
        
def Controls(stringinput):
    lines=stringinput.split("\\n")
    count=0
    Exchanges=[]
    while count<len(lines):#Separate every trips until no trips
        studentnumber=int(lines[count])#get the student number
        costlist=lines[count+1:count+studentnumber+1]#the cost of each student
        exchange=Mini_Exchange(costlist)#comput the exchange of one trip
        Exchanges.append(exchange)#store the result into a list named Exchanges
        count+=studentnumber+1#record the current line number
    PrintAmount(Exchanges)#Print out come in required form

        
        
if __name__ == "__main__":
    #Controls("2\\n3\\n10\\n4\\n1\\n100\\n60\\n78")
    Controls(sys.argv[1])
