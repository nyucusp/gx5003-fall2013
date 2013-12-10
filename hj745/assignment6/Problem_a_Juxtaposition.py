import pandas as pd
import matplotlib.pyplot as plt

#import data file and set the delimiter in the data file
data1 = pd.read_table('labeled_data.csv', sep=',', usecols=[0, 1, 2], index_col=['# zipcode'])
#the data is in the descending order, so it should be sorted with ascending order
result1 = data1.sort(ascending=True)

#For juxtaposition, I set the subplot as True
#plot the data
result1.plot(subplots=True,title='Problem a_labeled')
plt.show()

