import sys
import MySQLdb
# import warnings
# warnings.filterwarnings("ignore")

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                      user="rad416", # your username
                       passwd="mysql", # your password
                       db="coursedb") # name of the data base

with db:

  cur = db.cursor()

  query = "SELECT bp.borough, bi.borough_incidents/bp.borough_pop as incident_pop_ratio FROM( SELECT b.borough borough, SUM(total_population) borough_pop FROM zipcode_population zp INNER JOIN boroughs b ON b.zipcode = zp.zcta WHERE b.borough = '" + sys.argv[1] + "' GROUP BY b.borough ) as bp INNER JOIN ( SELECT b.borough borough, SUM(incidents) borough_incidents FROM incidents i INNER JOIN boroughs b ON b.zipcode = i.zipcode WHERE b.borough = '" + sys.argv[1] + "' GROUP BY b.borough ) as bi ON bi.borough = bp.borough"
  cur.execute(query)

  result = cur.fetchall()
  for row in result:
    if row[0] == "Staten":
      print "The ratio of incidents to population in " + row[0] + " Island is " + str(row[1])
    else:
      print "The ratio of incidents to population in " + row[0] + " is " + str(row[1])

db.close()