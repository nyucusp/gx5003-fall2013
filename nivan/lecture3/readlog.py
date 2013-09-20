myFile = open('logsofar.txt', 'r')
fileLines = myFile.readlines()

#print fileLines

authorCounter = {}
count = 0
for line in fileLines:
    indexOfCommmit = line.find('Author')
    if indexOfCommmit != -1:
        count = count + 1
        dictKeys = authorCounter.keys()
        if(line in dictKeys):
            authorCounter[line] = authorCounter[line] +1 
        else:
            authorCounter[line] = 1

dictKeys = authorCounter.keys()
sortedList = []
for key in dictKeys:
    sortedList.append((authorCounter[key], key))

y =  sorted(sortedList)

for x in y:
    print x
