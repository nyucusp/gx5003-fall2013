SELECT zipCodeData.zipcode, zipCodeData.population FROM coursedb.zipCodeData INNER JOIN coursedb.boroughs ON coursedb.zipCodeData.zipcode = coursedb.boroughs.zipcode INNER JOIN coursedb.incidents ON coursedb.zipCodeData.zipcode = coursedb.incidents.zipcode WHERE coursedb.boroughs.boroughName = "Manhattan";

