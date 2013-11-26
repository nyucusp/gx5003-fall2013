from pylab import * 
import numpy
from matplotlib import pyplot
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

def getresults(number):
    f = open("genes.dat","r")
    f.next()
    deney=[]
    for row in f:
        x = row.rstrip('\n').split(',')
        deney.append(float(x[number]))
    return deney

a = getresults(0)
b = getresults(1)
c = getresults(2)
d = getresults(3)

#1x1
ax1 = plt.subplot2grid((4,4), (0, 0))
plt.scatter(a, a, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene A vs. A', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#1x2
ax2 = plt.subplot2grid((4,4), (0, 3))
best3=np.polyfit(a,b,5)
xp = np.linspace(0,1,10000)
p = np.poly1d(best3)
plt.scatter(a, b, color = 'red', marker= '^', alpha=0.5)
plt.plot(xp, p(xp), 'r', label = '5th deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene A vs. B', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#1x3
ax3 = plt.subplot2grid((4,4), (0, 1))
best=np.polyfit(a,c,1)
xp = np.linspace(0,1,10000)
p = np.poly1d(best)
plt.scatter(a, c, color = 'blue', marker ='s', alpha = 0.5 )
plt.plot(xp, p(xp), 'r', label = '1st deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene A vs. C', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#1x4
ax4 = plt.subplot2grid((4,4), (0, 2))
best2=np.polyfit(a,d,2)
xp = np.linspace(0,1,10000)
p = np.poly1d(best2)
plt.scatter(a, d, color = 'green', marker ='D', alpha = 0.5 )
plt.plot(xp, p(xp), 'r', label = '2nd deg')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene A vs. D', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#2x1
ax5 = plt.subplot2grid((4,4), (1, 0))
plt.scatter(b, a, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene B vs. A', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#2x2
ax6 = plt.subplot2grid((4,4), (1, 3))
plt.scatter(b, b, color = 'red', marker= '^', alpha=0.5)
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene B vs. B', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#2x3
ax7 = plt.subplot2grid((4,4), (1, 1))
plt.scatter(b, c, color = 'blue', marker ='s', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene B vs. C', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#2x4
ax8 = plt.subplot2grid((4,4), (1, 2))
plt.scatter(b, d, color = 'green', marker ='D', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene B vs. D', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#3x1
ax9 = plt.subplot2grid((4,4), (2, 0))
plt.scatter(c, a, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene C vs. A', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#3x2
ax10 = plt.subplot2grid((4,4), (2, 3))
plt.scatter(c, b, color = 'red', marker= '^', alpha=0.5)
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene C vs. B', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#3x3
ax11 = plt.subplot2grid((4,4), (2, 1))
plt.scatter(c, c, color = 'blue', marker ='4', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene C vs. C', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#3x4
ax12 = plt.subplot2grid((4,4), (2, 2))
plt.scatter(c, d, color = 'green', marker ='D', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene C vs. D', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#4x1
ax13 = plt.subplot2grid((4,4), (3, 0))
plt.scatter(d, a, color = '0.25')
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene D vs. A', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#4x2
ax14 = plt.subplot2grid((4,4), (3, 3))
plt.scatter(d, b, color = 'red', marker= '^', alpha=0.5)
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene D vs. B', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#4x3
ax15 = plt.subplot2grid((4,4), (3, 1))
plt.scatter(d, c, color = 'blue', marker ='4', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene D vs. C', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})
#4x4
ax16 = plt.subplot2grid((4,4), (3, 2))
plt.scatter(d, d, color = 'green', marker ='D', alpha = 0.5 )
plt.axis([-0.1,1.1,-0.1,1.1])
plt.axis([-0.1,1.1,-0.1,1.1])
plt.title('Gene D vs. D', fontsize=11)
plt.legend(loc='upper left', prop={'size':5})

plt.tight_layout()
pyplot.savefig('problem4.png', dpi=200)
plt.show()
