import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime



def main():
##handle and organize data:	
	months = []
	apple = []
	msoft = []
	headers = True
	with open('stocks.dat', 'rb') as stocks:
		stockers = csv.reader(stocks)
		for row in stockers:
			if headers == True:
				headers = False
				continue
			months.append(row[0])
			apple.append(row[1])
			msoft.append(row[2])

	
	
##turn year/month into actual date
	dates = []
	for el in months:
		date = el.split('-')
		year = int(date[0])
		month = int(date[1])
		actualDate = datetime.date(year, month, 1)	
		dates.append(actualDate)

#Problem 1a
#I turned the dates provided in the file into the  "Month Year" format for readability
#This is a connected symbol plot
#uncomment the following code to show the plot:
	##plt.title("Apple's Stock Quotes")
	##plt.ylabel("Stock Quote")
	##plt.xlabel("Date")
	##plt.plot(dates, apple, 'o-')
	##plt.show() 


#problem 1b
#From this plot, you can clearly see that Apple is doing much
#better than Microsoft.
#uncomment the following code to show the plot:
	##plt.title("Apple vs Microsoft Stock Quotes")
	##plt.ylabel("Stock Quote")
	##plt.xlabel("Date")
	##p1, = plt.plot(dates,apple,label ="apple")
	##p2, = plt.plot(dates,msoft, label="msoft")
	##l1 = plt.legend([p1], ["Apple Stocks"], loc=0)
	##l2 = plt.legend([p2], ["Microsoft Stocks"], loc=4)	
	##plt.gca().add_artist(l1)
	##plt.show() 

#problem 1c
#I think that superposition makes more sense for this plot because
#the data is simple and easily comparable in the same plot.
#When they are in different plots, it is less apparent that 
#microsoft's stocks are well below apple's.

	
	plt.figure(1)
	plt.subplot(211)
	plt.plot(dates, apple, 'o-')	

	plt.title("Apple Stock Quotes")
	plt.ylabel("Stock Quote")
	plt.xlabel("Date")

	plt.subplot(212)
	plt.plot(dates, msoft, 'o-')

	##p1, = plt.plot(dates,apple,label ="apple")
	##p2, = plt.plot(dates,msoft, label="msoft")
	##plt.gca().add_artist(l1)
	
	plt.title("Microsoft Stock Quotes")
	plt.ylabel("Stock Quote")
	plt.xlabel("Date")

	plt.show() 



if __name__ == "__main__":
	main()
