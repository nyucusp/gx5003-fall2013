from decimal import *
#this is basically the same thing with what I did for question 2
class avgPop:
    def __init__(self, length, name, set1):
        length = length
        city = str(name)
        pop = 0
        counter = 0
        popboro = set1
        for i in range(0,length):
            x = list(popboro[i])
            if(x[1] == str('')):
                i = i+1
            elif(x[0] == str(city)):
                a = int(x[1])
                pop += a
                counter += 1
        self.a = pop/counter

    def __repr__(self):
        return "%s" % (self.a)
    
    def __str__(self):
        return "%s" % (self.a)
