import csv
from assignment6 import read_csv_to_dict
import numpy as np

cuspfilename = "labeled_data.csv"
irsfilename = "irs_zip_codes.csv"

cuspfields, cuspdata = read_csv_to_dict(cuspfilename)
input_zips = [ int(float(x['# zipcode'])) for x in cuspdata ]

irs_data = []
match = 0

# agi_class: 1 = 'Under $10,000' [1]; 2 = '$10,000 under $25,000'; 3 = '$25,000 under $50,000'
# 4 = '$50,000 under $75,000'; 5 = '$75,000 under $100,000'; 6 = '$100,000 under $200,000'
# 7 = '$200,000 or more
# N1    Number of returns [1]
# A00100    Adjust gross income (AGI) [2]
# A02300    Unemployment compensation [3]
with open(irsfilename, 'rb') as csvfile:
    datareader = csv.DictReader(csvfile)
    for row in datareader:
        if int(row['ZIPCODE']) in input_zips:
            irs_data.append( [int(row['ZIPCODE']), int(row['agi_class']), int(row['n1']), int(row['a00100']), int(row['a02300'])] )
            match += 1

# Write the results to a file.
with open("irs_ny_zips.csv", 'wb') as outptr:
    writer = csv.writer(outptr)
    writer.writerow(['zip', 'agi_class', 'num_returns', 'agi', 'unemployment_comp'])
    writer.writerows(irs_data)

