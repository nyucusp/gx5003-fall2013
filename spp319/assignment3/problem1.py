#readin file
myfile = open('input1.txt')

travelers = 0

def average():
    averageCost = (sum(totalcost)/len(totalcost))
    return averageCost


while True:
    travelers = int(myfile.readline())

    if travelers == 0:
        break
    totalcost = []

    #####
    for i in range( 0, travelers):
        c = float (myfile.readline())
        totalcost.append(c)
        average()
    #####

    diff = [x-float(average()) for x in totalcost]
    roundingfunc = [round(d,2) for d in diff]

    lower =[]

    for y in roundingfunc:
        if y < 0:
            lower.append(abs(y))

    print "%.2f" %float(sum(lower))


