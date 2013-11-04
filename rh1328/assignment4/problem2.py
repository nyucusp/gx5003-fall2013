import MySQLdb
import sys


def main():
	#assumes input is proper

	zipToCalculate = sys.argv[1]
	zipToCalculate = int(zipToCalculate)
        
	 #connect to database
        db = MySQLdb.connect(host="localhost", # your host, usually localhost
                              user="rh1328", # your username
                               passwd="cusppassword", # your password
                               db="coursedb") # name of the data base




	cursor = db.cursor()
	cursor.execute("""SELECT population FROM zipCodeData WHERE zipcode = %s """, (zipToCalculate,))
	population = cursor.fetchall()
	pop = population[0][0]

	cursor.execute("""SELECT area FROM zipCodeData WHERE zipcode = %s """, (zipToCalculate,))
	area = cursor.fetchall()
	areaNum = area[0][0]

        db.commit()
        db.close()


	density = pop/areaNum
	print density

if __name__ == "__main__":
	main()

