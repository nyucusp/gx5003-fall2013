from decimal import *

class numberOf:
    #defines the length of the population and incident sets
    #and calculates the incidents and population for each boro
    def __init__(self, length1, length2, name, set1, set2):
        length1 = length1
        length2 = length2
        city = str(name)
        incboro = set1
        popboro = set2
        incbrx = 0
        popbrx = 0
        for i in range(0,length1):
            x= list(incboro[i])
            if(x[1] == str('')):
                i=i+1
            elif(x[0] == str(city)):
                a = int(x[1])
                incbrx += a
        for i in range(0,length2):
            x= list(popboro[i])
            if(x[1] == str('')):
                i=i+1
            elif(x[0] == str(city)):
                a = int(x[1])
                popbrx += a
        self.a = Decimal(incbrx)/(popbrx)

    def __repr__(self):
        return "%s" % (self.a)
    
    def __str__(self):
        return "%s" % (self.a)





