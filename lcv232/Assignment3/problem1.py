import sys
d={}
while(True):
    a=input("")   
    if (int(a) <= 1000):
        if (int(a) != 0):
            L=[]
            for i in range(a):
                b=input("")
                if (float(b) <= 10000.00):
                    if isinstance(b, float):
                        L.append(b)
                
                    else:
                        if (int(b) == 0):
                            break
                        else:
                            break
            d[a]=L
        elif (int(a) == 0):
            break
print "OUTPUT"
for data in d.keys():
    a=0
    for dt in d[data]:
        a=int(a)+int(dt)
    print  float(a/data)