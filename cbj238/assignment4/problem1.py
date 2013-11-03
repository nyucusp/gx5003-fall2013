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

def get_sql_column(name, vartype, primary_key):
    retStr = "{0} ".format(name)
    if vartype==int:
        retStr += "int"
    elif vartype==float:
        retStr += "float(6)"
    else:
        retStr += "varchar(255)"

    if (primary_key == name) and (vartype==int):
        retStr += " not null"

    print retStr

    return retStr

def create_schema_from_header(tableName, data, primary_key):
    # print "Schema:", tableName, data[0], data[1]
    # All we need are the names and types for each field.

    # Error checking: make sure no column names have spaces
    for name in data[0]:
        if name.find(' ') != -1:
            name.replace(' ', '_')

    primary_key_str = primary_key
    createCommand = "create table " + tableName + " ("
    if primary_key is None:
        createCommand += "id int not null, "
        primary_key_str = "id"
    items = []
    for index in xrange(len(data[0])):
        items.append( get_sql_column(data[0][index], data[1][index], primary_key) )

    createCommand += ", ".join([x for x in items]) + ", primary key({0}))".format(primary_key_str)

    print createCommand

    return createCommand

def insert_data_from_contents(tableName, data):
    # print "Data:", tableName, len(data[1])
    # for index in xrange(len(data[1])):
    #     print data[1][index]#, data[2][index]
    return None

def csv_to_db(csvData, tableName, primary_key=None):
    ''' Takes a ParseCSV object and the table to create,
    and creates and populates the table from the csv data.

    - The table schema is created from the header data.
    '''
    db = dbMgr()
    data = csvData.getRawData()
    
    create_schema = create_schema_from_header(tableName, data, primary_key)
    # db.run_sql(create_schema)

    insert_data = insert_data_from_contents(tableName, data)
    # db.run_sql(insert_data)

    db.close()
    

def main():
    # Read in and parse all the CSV files.
    boroughFile = ParseBoroughsCSV()
    zipFile = ParseZipCodesCSV()
    incidentsFile = ParseIncidentsCSV()

    csv_to_db(boroughFile, BOROUGHS_TABLE, "zipcode")
    csv_to_db(zipFile, ZIP_TABLE)
    csv_to_db(incidentsFile, INCIDENTS_TABLE)

if __name__ == "__main__":
    main()
