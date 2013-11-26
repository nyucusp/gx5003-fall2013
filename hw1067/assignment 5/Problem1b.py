# -*- coding: utf-8 -*-
#Assignment 5
#Problem1 B
#Haozhe Wang

import pandas as pd
import csv
import pylab
import numpy as np
import matplotlib.pyplot as plt


stockfile = pd.read_csv('stocks.dat')#read the file with pandas call function
#print stockfile

index = stockfile.set_index('month')
#print index


right_timeseq = index.sort()


prefig = right_timeseq.plot(legend = True, style = "^--")
#configure the plot
prefig.set_title('MSFT vs. AAPL')
prefig.xaxis.grid(True, which="minor")
prefig.xaxis.grid(True, which="major")
prefig.set_ylabel('Price')
prefig.set_xlabel('Month')
#prefig.annotate('Used Pandas and matplotlib to sort\n "month" as index, and configured\n other factors a little bit.', xy=(16,75))
#plt.tight_layout()
plt.axhline(y = 27.06, color = "k")
plt.axhline(y = 75.51, color = "k")

plt.annotate("USD27.06 in\n Jan 2006",xy=(28,38),fontsize = 10, color = "g")#annotate the baseline with font size 10 on top of the actual line in green 
plt.annotate("USD75.51 in\n Jan 2006",xy=(28,84),fontsize = 10, color = "b")


prefig.figure.savefig('MandA.jpg',dpi = 300)

"""
the two stocks were plotted as two seperate inputs. Without Pandas, I changed fonts, and added annotation.
two threshould lines were added to show where each of them started,  and how they were performing along the time.
Annotations were by the lines to show wht the price was for each stock.
"""

