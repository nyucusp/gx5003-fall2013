myFile = open("input1.txt", "r")

def readFile():
    groupSize = 0
    #put file into an array:
    string = myFile.readlines()
    arr = []
    eachGroup = []
    for i in string:
        if i != "\n":
            #all items in list are now floats and \n characters are ommitted
            arr.append(float(i.rstrip('\n')))
    for a in arr:
        groupSize = arr[0]
        #after taking care of each number, pop it off of the List
        del arr[0]
        for s in range(int(groupSize)):
            #append to the eachGroup List the amount each person spent in that group
            eachGroup.append(arr[0])
            del arr[0]
        calculate(eachGroup, groupSize)
        #clear the eachGroup array to use for other groups contained in the file
        del eachGroup[:]
        

def calculate(arr, groupSize):
    totalSpent = 0
    totalForEach = 0
    amtToExchange = 0
    for index in arr:
        #add up total amount spent 
        totalSpent += index
        #figure out how much each person should have spent
        totalForEach = float(totalSpent)/float(groupSize)
    for temp in arr:
        #if a person paid less than their share, they need to exchange money
        if temp < totalForEach:
            amtToExchange += (float(totalForEach) - float(temp))
    print float(amtToExchange)


def main():
    readFile()



if __name__ == "__main__":
    main()
