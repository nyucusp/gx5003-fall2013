import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict

data_temp = open('labeled_data.csv','r')
data = csv.DictReader(data_temp,['# zip_code','population','num_incidents'])
zip_codes = []
popul = []
num_inc = []

for item in data:
    zip_codes.append(item['# zip_code'])
    popul.append(item['population'])
    num_inc.append(item['num_incidents'])

del zip_codes[0]
del popul[0]
del num_inc[0]
zip_codes = [int(float(val)) for val in zip_codes]
popul = [int(float(val)) for val in popul]
num_inc = [int(float(val)) for val in num_inc]

#Dictionary creation
zip_codes_dict = {}
i = 0
while i < len(zip_codes):
    zip_codes_dict[zip_codes[i]]= num_inc[i]
    i= i + 1
zip_codes_dict = OrderedDict(sorted(zip_codes_dict.items()))

#List creation
zip_codes = []
inc_by_zip_code = []
for k, v in zip_codes_dict.items():
    zip_codes.append(k)
    inc_by_zip_code.append(v)

#1st Chart
plt.scatter(popul, num_inc, color='black')
plt.title('Population / 311 Calls in NYC')
plt.xlim((-1500,120000))
plt.ylim((-2500,max(num_inc)+1000))
plt.xlabel('Population')
plt.ylabel('# of 311 Calls')
plt.show()

#2nd Chart
dummy_list = np.arange(0,len(zip_codes), 1)
plt.bar(dummy_list, inc_by_zip_code, 1, color='green')
plt.title('Zip Code / 311 Calls in NYC')
zip_code_ticks = zip_codes[::10]
plt.xticks(np.arange(1,len(zip_codes),10),zip_code_ticks, rotation=20)
plt.xlabel('NYC Zip Code')
plt.ylabel('# of 311 Calls')
plt.show()