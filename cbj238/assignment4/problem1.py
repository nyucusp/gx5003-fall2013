import MySQLdb
from parsecsv import *

BOROUGHS_TABLE="boroughs"
ZIP_TABLE="zipcodes"
INCIDENTS_TABLE="incidents"

class dbMgr:
    def __init__(self):
        #connect to database
        self.db = MySQLdb.connect(host="localhost",
                             user="cbj238",
                             passwd="1122334455",
                             db="coursedb")
        
        # The Cursor object lets you execute the sql commands
        self.cur = self.db.cursor()

    def run_sql(self, command):
        if command is not None and len(command) > 0:
            self.cur.execute(command)

    def close(self):
        # Must commit changes before closing connection Else data won't be inserted.    
        self.db.commit()

        # Close the connection
        self.db.close()

def create_schema_from_header(tableName, data):
    print "Schema:", tableName, data[0], data[1]
    return None

def insert_data_from_contents(tableName, data):
    # print "Data:", tableName, len(data[1])
    # for index in xrange(len(data[1])):
    #     print data[1][index]#, data[2][index]
    return None

def csv_to_db(csvData, tableName):
    ''' Takes a ParseCSV object and the table to create,
    and creates and populates the table from the csv data.

    - The table schema is created from the header data.
    '''
    db = dbMgr()
    data = csvData.getRawData()
    
    create_schema = create_schema_from_header(tableName, data)
    db.run_sql(create_schema)

    insert_data = insert_data_from_contents(tableName, data)
    db.run_sql(insert_data)

    db.close()
    

def main():
    # Read in and parse all the CSV files.
    boroughFile = ParseBoroughsCSV()
    zipFile = ParseZipCodesCSV()
    incidentsFile = ParseIncidentsCSV()

    csv_to_db(boroughFile, BOROUGHS_TABLE)
    csv_to_db(zipFile, ZIP_TABLE)
    csv_to_db(incidentsFile, INCIDENTS_TABLE)

if __name__ == "__main__":
    main()
