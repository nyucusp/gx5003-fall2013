import MySQLdb
from parsecsv import *

BOROUGHS_TABLE="boroughs"
ZIP_TABLE="zipcodes"
INCIDENTS_TABLE="incidents"

class dbMgr:
    def __init__(self):
        try: 
            #connect to database
            self.db = MySQLdb.connect(host="localhost",
                                 user="cbj238",
                                 passwd="1122334455",
                                 db="coursedb")

            self.cur = self.db.cursor() 
        except MySQLdb.Error:
            print "There was a problem in connecting to the database. Please ensure tha tthe database exists on the local host system."
            exit(-1)

    def run_sql(self, command):
        if command is not None and len(command) > 0:
            # The Cursor object lets you execute the sql commands

            try: 
                self.cur.execute(command)

            # self.cur.close()
             # OperationalError
            except MySQLdb.OperationalError, e :
                print "Some of the information you have passed is not valid. Please check it before trying to use this program again. You may also use '-h' to see the options available."
                print "The exact error information reads as follows:%s" %(e)
                raise
            # DataError
            # ProgrammingError
            except (MySQLdb.DataError, MySQLdb.ProgrammingError), e:
                print "An irrecoverable error has occured in the way your data was to be processed. This application must now close. An error message describing the fault has been sent to the development team. Apologies for any inconvenience."
                raise
            # IntegrityError
            except MySQLdb.IntegrityError, e:
                print "An irrecoverable database error has occurred and this process must now end. An error message describing the fault has been sent to the database administrator. Apologies for any inconvenience."
                raise
            # InternalError
            # NotSupportedError
            except (MySQLdb.InternalError, MySQLdb.NotSupportedError), e:
                print "An irrecoverable error has occurred and this process must now end. An error message describing the fault has been sent to the appropriate staff. Apologies for any inconvenience."
                raise
            except MySQLdb.Warning:
                pass

    def commit(self):
        # Must commit changes before closing connection Else data won't be inserted.    
        self.db.commit()

    def close(self):

        # Close the connection
        self.db.close()

def clean_db(db):
    try:
        clean_command = "DROP TABLE IF EXISTS zipcodes"
        db.run_sql(clean_command)
        clean_command = "DROP TABLE IF EXISTS incidents"
        db.run_sql(clean_command)
        clean_command = "DROP TABLE IF EXISTS boroughs"
        db.run_sql(clean_command)
        db.commit()
    except MySQLdb.Warning:
        # Just ignore those warnings about them not existing.
        pass

def get_sql_column(name, vartype, primary_key):
    retStr = "{0} ".format(name)

    if vartype=="INT":
        retStr += "int"
    elif vartype=="FLOAT":
        retStr += "float(6)"
    else:
        retStr += "varchar(255)"

    if (primary_key == name) and (vartype==int):
        retStr += " not null"

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
    return gettype(cell)[0] == columntype

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

    print "{0} Valid entries".format(len(entries))
    print "{0} Invalid entries".format(len(invalidEntries))
    # for entry in invalidEntries:
    #     print entry

    return entries

def insert_data_from_contents(db, tableName, data):
    column_list = build_column_list(data[0])
    data_list = build_data_list(data[2], data[1])
    
    for row in data_list:
        insert_query = "INSERT INTO {0} ({1}) VALUES {2}".format(tableName, column_list, row)
        db.run_sql(insert_query)

def csv_to_db(db, csvData, tableName, primary_key=None):
    ''' Takes a ParseCSV object and the table to create,
    and creates and populates the table from the csv data.

    - The table schema is created from the header data.
    '''
    
    data = csvData.getRawData()
    print "Creating {0}. {1} records in csv.".format(tableName, len(data[2][0]))

    # Error checking: make sure no column names have spaces
    for name in data[0]:
        if name.find(' ') != -1:
            name.replace(' ', '_')
    
    create_schema = create_schema_from_header(tableName, data, primary_key)
    print create_schema
    db.run_sql(create_schema)
    db.commit()

    insert_data_from_contents(db, tableName, data)
    db.commit()
    

def main():
    db = dbMgr()
    # Clean out the previous tables...
    clean_db(db)

    # Read in and parse all the CSV files.
    boroughFile = ParseBoroughsCSV()
    zipFile = ParseZipCodesCSV()
    incidentsFile = ParseIncidentsCSV()

    csv_to_db(db, boroughFile, BOROUGHS_TABLE)
    csv_to_db(db, zipFile, ZIP_TABLE)
    csv_to_db(db, incidentsFile, INCIDENTS_TABLE)

    db.close()

if __name__ == "__main__":
    main()
