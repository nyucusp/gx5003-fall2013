import sys

myFile = open('input1.txt','r')
n = 100

while n != 0:
    n = int(myFile.readline())
    if (n == 0):
        sys.exit()
    total = 0
    count = 0
    amountpaid = []
    while count < n:
        value = myFile.readline().strip('\n')
        total += float(value)
        count += 1
        amountpaid.append(value)
    avg_money = total/n

    i = 0
    totalexchange = 0
    while i < n:
        totalpaid = float(amountpaid[i])
        if (totalpaid < avg_money):
            difference = avg_money - totalpaid
            totalexchange += difference
        i += 1
    print totalexchange

myFile.close()
