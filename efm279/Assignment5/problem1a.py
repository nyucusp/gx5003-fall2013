
import matplotlib.pyplot as plt
import numpy as np
import csv
x1 = []
y1 = []
xcount=[]
counter=0

with open('stocks.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    spamreader.next() 
    for row in spamreader:
            y1.append(row[1])
            x1.append(row[0])
            counter=counter+10
            xcount.append(counter)    

xv = np.array(x1)
yv = np.array(y1)
xc= np.array(xcount)



maxint=float(max(y1,key=float))
maxindex=y1.index(max(y1,key=float))
minint=float(min(y1,key=float))
minindex=y1.index(min(y1,key=float))
fig=plt.figure(figsize=(18, 18))
ax=fig.add_subplot(111)
ax.annotate('maximum value', xy=(xcount[maxindex],maxint), xytext=(xcount[maxindex]+10,maxint+10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax.annotate('minimum value', xy=(xcount[minindex],minint), xytext=(xcount[minindex]-10,minint-10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.set_ylim(40,220)

plt.plot(xc,y1,color='green', linestyle='-', marker='o',markerfacecolor='blue', markersize=6)
plt.xticks(xc,x1,rotation='vertical')
plt.ylabel("Apple Stock Value ($)")
plt.xlabel("Year-Month")
plt.gca().invert_xaxis()
plt.grid(True)
plt.title('Apple Stock Value Performance Jan06-Sep08')
plt.show()


## According to this plot Apple stocks have an increasing trend since January 2006 except the recession year 2008.
# Maximum value is observed in December 2007 right before the recession and minimum value during this period is in June 2006
