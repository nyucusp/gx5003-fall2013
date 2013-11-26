import matplotlib.pyplot as plt
import pylab   

# read the stocks data
stocks = open('stocks.dat','r')

# create empty lists to append the data
Apple = []
Month = []
Microsoft = []
lines = 34 #to combat the months being backwards, I just chose to count backwards starting with 34

stocks.readline() # skip first row

for row in stocks: #this will read the stock quotes as floats and makes Months appear as intergers.
	fields = row.strip().split(",") #make into fields
	Apple.append(float(fields[1]))
	Microsoft.append(float(fields[2]))
	lines = lines - 1
	Month.append(int(lines))


#first scatter plot of apple stock
plt.plot(Month, Apple, marker='o', linestyle='--', color = 'g', label  = 'Apple')
plt.xlabel('Months Jan 2006 - Aug 2008')
plt.ylabel('Stock Price ($)')
plt.title('Apple Stock Prices')
plt.xticks(range(1,34,4))
plt.legend(loc=2)
plt.show()

