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
            x1.append(row[0][2:])
            counter=counter+10
            xcount.append(counter)    

xv = np.array(x1)
yv = np.array(y1)
yw = np.array(y2)
xc = np.array(xcount)



fig=plt.figure(figsize=(17, 17))


ax1=plt.subplot(211)
ax2=plt.subplot(212,sharex=ax1)

ax1.set_ylim(0,250)
ax2.set_ylim(0,60)


maxint=float(max(y1,key=float))
maxindex=y1.index(max(y1,key=float))
minint=float(min(y1,key=float))
minindex=y1.index(min(y1,key=float))

maxint2=float(max(y2,key=float))
maxindex2=y2.index(max(y2,key=float))
minint2=float(min(y2,key=float))
minindex2=y2.index(min(y2,key=float))

ax1.annotate('maximum value', xy=(xcount[maxindex],maxint), xytext=(xcount[maxindex]+10,maxint+10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax1.annotate('minimum value', xy=(xcount[minindex],minint), xytext=(xcount[minindex]-10,minint-10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax2.annotate('maximum value', xy=(xcount[maxindex2],maxint2), xytext=(xcount[maxindex2]+10,maxint2+10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
ax2.annotate('minimum value', xy=(xcount[minindex2],minint2), xytext=(xcount[minindex2]-10,minint2-10),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax1.plot(xc,y1,color='green', linestyle='-', marker='o',markerfacecolor='green', markersize=6, label='apple')
ax2.plot(xc,y2,color='red', linestyle='-', marker='o',markerfacecolor='red', markersize=6, label='microsoft')

blindex=x1.index('06-01')
ax1.axhline(y=y1[blindex],ls='--',color='green',label='January 2006')
ax2.axhline(y=y2[blindex],ls='--',color='red',label='January 2006')

ax1.xaxis.set_ticks(xc)

for ax in ax1, ax2:
    ax.grid(True)
    ax.set_xlabel('Year-Month')    
    ax.set_ylabel('Stocks')
    ax.xaxis.set_ticks(xc)
    ax.set_xticklabels(x1,rotation='vertical')
    ax.set_xlim(0,340)

ax1.legend(('Apple','Apple Jan 2006'))
ax2.legend(('Microsoft','Microsoft Jan 2006'))
ax1.set_title(('(a)Apple Stock Performance Jan 2006-Sep 2008, (b)Microsoft Stock Performance Jan 2006-Sep 2008'))
#ax2.set_title(('Microsoft Stock Performance Jan 2006-Feb 2008')) 

plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()

## Now this graph is better than superpostion since we can clearly see what is going on in both stocks with different y scales.
## Now we see the correlation between the two stocks both reached their maximum within about Fall 2007
## Then both stocks decreased due to recession and in August 2008 both stocks slightly increased.
## In superposition graph you can clearly see the value difference but you cannot see the detailed changes in both stocks at the same time due to scaling 

