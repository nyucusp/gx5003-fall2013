import matplotlib.pyplot as plt
import pylab   

stocks = open('stocks.dat','r')

# create empty lists to append the data
Apple = []
Month = []
Microsoft = []
lines = 34 #to combat the months being backwards, I just chose to count backwards starting with 34

stocks.readline() # skip first row

for row in stocks: #this will read the stock quotes as floats and makes Months appear as intergers (using lines)
	fields = row.strip().split(",") #make into fields
	Apple.append(float(fields[1]))
	Microsoft.append(float(fields[2]))
	lines = lines - 1
	Month.append(int(lines))


#sub-scatter plot of Apple stock
plt.subplot(2,1,1)
plt.plot(Month, Apple, marker='o', linestyle='--',color = 'g', label  = 'Apple')
plt.title('Stock Price Charts')
plt.ylabel('Apple Stock Price ($)')
plt.xticks(range(1,34,4))

#sub-scatter plot of Microsoft stock
plt.subplot(2,1,2)
plt.plot(Month, Microsoft,marker='o', linestyle='--', color = 'r', label = 'Microsoft')
plt.xlabel('Month Jan 2006 - Aug 2008')
plt.ylabel('Microsoft Stock Price ($)')
plt.xticks(range(1,34,4))

plt.show()

