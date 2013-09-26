from zipcode import Zipcode
from borough import Borough

boroughs['manhattan'] = Borough('manhattan')

zipcode = Zipcode(value_read_from_csv)
boroughs['manhattan'].addZipcode(zipcode)
