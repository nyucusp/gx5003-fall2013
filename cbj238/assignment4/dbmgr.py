"""
    assignment 4
    author: Christopher Jacoby
    Principles of Urban Informatics, Fall 2013
"""

import MySQLdb

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

    def results(self):
        return self.cur.fetchall()

    def commit(self):
        # Must commit changes before closing connection Else data won't be inserted.    
        self.db.commit()

    def close(self):

        # Close the connection
        self.db.close()