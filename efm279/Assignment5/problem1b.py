
import matplotlib.pyplot as plt
import numpy as np
import csv
x1 = []
y1 = []
y2 = []
xcount=[]
counter=0

with open('stocks.dat', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    spamreader.next() 
    for row in spamreader:
            y1.append(row[1])
            y2.append(row[2])
            x1.append(row[0])
            counter=counter+10
            xcount.append(counter)    

xv = np.array(x1)
yv = np.array(y1)
yw = np.array(y2)
xc = np.array(xcount)



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

ax.set_ylim(0,220)
#ax.set_xlim(-50,220)

p1=plt.plot(xc,y1,color='green', linestyle='-', marker='o',markerfacecolor='green', markersize=6, label='apple')
p2=plt.plot(xc,y2,color='red', linestyle='-', marker='o',markerfacecolor='red', markersize=6, label='microsoft')
plt.xticks(xc,x1,rotation='vertical')
plt.ylabel("Stock Value ($)")
plt.xlabel("Year-Month")

blindex=x1.index('2006-01')
plt.axhline(y=y1[blindex],ls='--',color='green',label='January 2006',linewidth='1.5')
plt.axhline(y=y2[blindex],ls='--',color='red',label='January 2006',linewidth='1.5')
plt.legend(('Apple','Microsoft','Apple Jan 2006','Microsoft Jan 2006'))
plt.gca().invert_xaxis()
plt.grid(True)
plt.title('Stock Value Performance Jan 06- Sep 08')
plt.show()

# This graph shows that Microsoft has a rather stable stock value compared to Apple.
# The value of Microsoft stock is lower in September 2008 compared to the base value January 2006
# Apple performs a lot better after September 2006 although there is an obvious decrease between base value Jan 2006 and Sep 2006. 
# Apple stock value has alwas been higher than Microsoft during this period.
# Increases and decreases are rather correlated but due to scaling Microsoft's performance is not quite clear.

