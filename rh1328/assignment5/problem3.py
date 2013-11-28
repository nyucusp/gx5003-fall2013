import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime
 
 
 
def main():
##handle and organize data:     
        year = []
        transistors = []
        processor = []
        headers = True
        with open('microprocessors.dat', 'rb') as fles:
                reads = csv.reader(fles)
                for row in reads:
                        if headers == True:
                                headers = False
                                continue
                        processor.append(row[0])
                        year.append(int(row[1]))
                        transistors.append(int(row[2]))

	#set name to a number for plotting
	numeric = []
	for i in range(len(processor)):
		print str(i) + "=" +  processor[i]
		numeric.append(i)


        plt.figure(1)
        plt.subplot(121)
        plt.plot(numeric, year, 'o')

#0=Pentium 4 processor
#1=286
#2=Pentium processor
#3=Xeon
#4=8080
#5=8008
#6=4004
#7=486TM DX processor
#8=8086
#9=386TM processor
##10=Pentium III processor
#11=Itanium
#12=Pentium II processor



        plt.title("Processors vs Year")
        plt.ylabel("Year")
        plt.xlabel("Processor (number relates to name)")
        plt.subplot(122)
        plt.plot(numeric, transistors, 'o')

	plt.yscale('log')
        plt.title("Processors vs Transistors")
        plt.ylabel("Transistors")
        plt.xlabel("Processor")

	plt.show()

if __name__ == "__main__":
	main()
