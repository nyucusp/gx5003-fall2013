import MySQLdb
import sys



def main():
        #assumes input is proper

        boroughName = sys.argv[1]
         #connect to database

        db = MySQLdb.connect(host="localhost", # your host, usually localhost
                              user="rh1328", # your username
                               passwd="cusppassword", # your password
                               db="coursedb") # name of the data base


        cursor = db.cursor()
        cursor.execute("""select count(address) FROM coursedb.boroughs INNER JOIN coursedb.incidents ON coursedb.boroughs.zipcode=coursedb.incidents.zipcode WHERE boroughName = %s;""", (boroughName,))
#"SELECT population FROM zipCodeData WHERE zipcode = %s """, (zipToCalculate,))
        numIncidents = cursor.fetchall()
        numIncidents = numIncidents[0][0]



	cursor.execute("""SELECT  sum(zipCodeData.population) FROM coursedb.zipCodeData INNER JOIN coursedb.boroughs ON coursedb.zipCodeData.zipcode = coursedb.boroughs.zipcode WHERE coursedb.boroughs.boroughName = %s;""", (boroughName,));
        population = cursor.fetchall()
        population = population[0][0]

        db.commit()
        db.close()
	
	ratio = numIncidents/population
	print ratio


if __name__ == "__main__":
        main()

