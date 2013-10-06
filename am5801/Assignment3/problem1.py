# Awais Malik
# Assignment 3
# Problem 1

from decimal import *

travels = open('input1.txt','r')
log = []
amounts = []

for line in travels:
    log.append(line.strip())
    
for line in log:
    if(line.find(".") == -1):
        students = int(line)
        count = 0
    else:
        amounts.append(Decimal(line))
        count += 1
        if(count == students):
            tot_exp = sum(amounts)
            average = (tot_exp/students).quantize(Decimal('.01'), rounding=ROUND_UP)
            total = 0
            for line in amounts:                
                if(line > average):
                    diff = abs(line - average)
                    total += diff
            print str(total)
            amounts = []