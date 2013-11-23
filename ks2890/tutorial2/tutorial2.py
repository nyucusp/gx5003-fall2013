import zipcode
import borough
boroughs = open('boroughs.csv', 'r')

boroughs['manhattan'] = Borough('manhattan')

zipcode = Zipcode(value_read_from_csv)
boroughs['manhattan'].addZipcode(zipcode)
