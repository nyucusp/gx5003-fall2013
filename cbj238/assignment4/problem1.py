import MySQLdb
from parsecsv import ParseCSV

BOROUGHS_FILE="boroughs.csv"
BOROUGHS_TABLE="boroughs"

ZIP_FILE="zipCodes.csv"
ZIP_TABLE="zipcodes"

INCIDENTS_FILE="Incidents_grouped_by_Address_and_Zip.csv"
INCIDENTS_TABLE="incidents"

class dbMgr:
    def __init__(self):
        #connect to database
        self.db = MySQLdb.connect(host="localhost",
                             user="cbj238",
                             passwd="1122334455",
                             db="coursedb")
        
        # The Cursor object lets you execute the sql commands
        self.cur = db.cursor()

    def run_sql(self, command):
        if len(command) > 0 and command is not None:
            cur.execute(command)

    def close(self):
        # Must commit changes before closing connection Else data won't be inserted.    
        self.db.commit()

        # Close the connection
        self.db.close()

def create_schema_from_header(tableName, data):
    print "Schema:", tableName, data.keys()
    return None

def insert_data_from_contents(tableName, data):
    print "Data:", tableName, len(data)
    return None

def csv_to_db(csvData, tableName):
    ''' Takes a ParseCSV object and the table to create,
    and creates and populates the table from the csv data.

    - The table schema is created from the header data.
    '''
    db = dbMgr()
    data = csvData.getLabelledData()
    
    create_schema = create_schema_from_header(tableName, data)
    db.run_sql(chreate_schema)

    insert_data = insert_data_from_contents(tableName, data)
    db.run_sql(insert_data)

    db.close()
    

def main():
    # Read in and parse all the CSV files.
    boroughFile = ParseCSV(BOROUGHS_FILE)
    zipFile = ParseCSV(ZIP_FILE)
    incidentsFile = ParseCSV(INCIDENTS_FILE)

    csv_to_db(boroughFile, BOROUGHS_TABLE)
    csv_to_db(zipFile, ZIP_TABLE)
    csv_to_db(incidentsFile, INCIDENTS_TABLE)

if __name__ == "__main__":
    main()
