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

    def run_sql(self, command):
        if command is not None and len(command) > 0:
            # The Cursor object lets you execute the sql commands
            self.cur = self.db.cursor()

            self.cur.execute(command)

            self.cur.close()

    def close(self):
        # Must commit changes before closing connection Else data won't be inserted.    
        self.db.commit()

        # Close the connection
        self.db.close()

def clean_db(db):
    clean_command = "DROP TABLE IF EXISTS zipcodes"
    db.run_sql(clean_command)
    clean_command = "DROP TABLE IF EXISTS incidents"
    db.run_sql(clean_command)
    clean_command = "DROP TABLE IF EXISTS boroughs"
    db.run_sql(clean_command)

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

    # print retStr

    return retStr

def create_schema_from_header(tableName, data, primary_key):
    # print "Schema:", tableName, data[0], data[1]
    # All we need are the names and types for each field.

    primary_key_str = primary_key
    createCommand = "create table " + tableName + " ("
    if primary_key is None:
        createCommand += "id int NOT NULL AUTO_INCREMENT, "
        primary_key_str = "id"
    items = []
    for index in xrange(len(data[0])):
        items.append( get_sql_column(data[0][index], data[1][index], primary_key) )

    createCommand += ", ".join([x for x in items]) + ", primary key({0}))".format(primary_key_str)

    # print createCommand

    return createCommand

def build_column_list(columns):
    return ", ".join(columns)

def is_valid_cell(cell, columntype):
    return gettype(cell) == columntype

def build_data_list(data, types):
    entries = []
    invalidEntries = []
    col_count = len(data)

    # iterate over the entris in the csv
    for i in xrange(len(data[0])):
        entry = []
        isValid = True
        #iterate over the columns
        for j in xrange(col_count):
            cell = data[j][i]

            isValid &= is_valid_cell(cell, types[j])

            entry.append("'" + cell + "'")

        entryStr = "(" + ", ".join(entry) + ")"

        if isValid:
            entries.append( entryStr )
        else:
            invalidEntries.append( entryStr ) 

    print "{0} Invalid entries".format(len(invalidEntries))
    for entry in invalidEntries:
        print entry

    return entries

def insert_data_from_contents(tableName, data):
    column_list = build_column_list(data[0])
    data_list = build_data_list(data[2], data[1])
    
    for row in data_list:
        try:
            insert_query = "INSERT INTO {0} ({1}) VALUES {2}".format(tableName, column_list, data_list)
            # print insert_query
            # db.run_sql(insert_query)
        except:
            print "Exception at query: {0}".format(insert_query)

def csv_to_db(db, csvData, tableName, primary_key=None):
    ''' Takes a ParseCSV object and the table to create,
    and creates and populates the table from the csv data.

    - The table schema is created from the header data.
    '''
    
    data = csvData.getRawData()

    # Error checking: make sure no column names have spaces
    for name in data[0]:
        if name.find(' ') != -1:
            name.replace(' ', '_')
    
    create_schema = create_schema_from_header(tableName, data, primary_key)
    db.run_sql(create_schema)

    insert_data_from_contents(tableName, data)
    

def main():
    db = dbMgr()
    # Clean out the previous tables...
    clean_db(db)

    # Read in and parse all the CSV files.
    boroughFile = ParseBoroughsCSV()
    # zipFile = ParseZipCodesCSV()
    # incidentsFile = ParseIncidentsCSV()

    csv_to_db(db, boroughFile, BOROUGHS_TABLE)
    # csv_to_db(db, zipFile, ZIP_TABLE)
    # csv_to_db(db, incidentsFile, INCIDENTS_TABLE)

    db.close()

if __name__ == "__main__":
    main()
