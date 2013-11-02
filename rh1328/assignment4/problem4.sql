select address from coursedb.incidents, coursedb.boroughs where coursedb.incidents.zipcode = coursedb.boroughs.zipcode and coursedb.boroughs.boroughname = "Manhattan";

