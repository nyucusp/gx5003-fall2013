import pandas as pd
import matplotlib.pyplot as plt

#import data file and set the delimiter in the data file
data = pd.read_table('stocks.dat', sep=',',usecols=[0, 1, 2], index_col=['month'])
#the data is in the descending order, so it should be sorted with ascending order  
result = data.sort(ascending=True)

#plot the data
result.plot(title='Problem_1b')
plt.show()

#this line is to save figure as *.png format, but the image file comes as white without any graph so that I don't use this code 
#plt.savefig('Problem_1b.png')
