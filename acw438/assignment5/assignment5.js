var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);

var svg = d3.select('#div1').append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// -----------------------------------------------------------------------------

var bike_data = []
var station_data = []

var data_array = [json1,json2,json3,json4,json5,json6]
data_array.forEach(function(row, index, arr) {bike_data.push([row['executionTime'].split(' ')[1]]);})

//var time_template = bike_data;
var time_template = jQuery.extend(true, [], bike_data);
var time_domain = bike_data.map(function(value, index) {return value[0]})
console.log("Query times: ", time_domain);

var highest_y = 0;

// Build station list
json1.stationBeanList.forEach(function(row, index, arr) {
	var templist = jQuery.extend(true, [], time_template);
	templist.push(row.stationName);
	station_data.push(templist);
	});

data_array.forEach(function(row, index, arr) {

	// Build total available bike count ----------------------------
	var totbikes = d3.sum(row.stationBeanList, function (station) {
		return station.availableBikes;
		});
	if (totbikes > highest_y) {
		highest_y = totbikes
		}
	bike_data[index].push(totbikes);

	// There is the same number of stations per datagrab
	// console.log(row.stationBeanList.length);

	// Build station available bike counts -------------------------
	row.stationBeanList.forEach(function(stat_row, stat_index, stat_arr) {
		station_data[stat_index][index][1] = stat_row.availableBikes;
	});
});

console.log("Available bikes: ", bike_data.map(function(value,index) {return value[1]}));
console.log("Here is the normal bike data", bike_data);
console.log("Here is the bike station data", station_data);

x.domain(time_domain);
y.domain([0, highest_y]);

svg.append("g")
	.attr("class", "y axis")
    .call(yAxis)
    
svg.append("g")
	.attr("class", "x axis")
	.attr("transform", "translate(0," + height + ")")
	.call(xAxis);

svg.selectAll(".bar")
    .data(bike_data)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) { return x(d[0]); })
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d[1]); })
    .attr("height", function(d) { return height - y(d[1]); });

// -------------------------------------------------------------------------

stationNames = station_data.map(function(value, index) {return value[6]});
console.log(stationNames);

var station_DOM = d3.select('#div2')
	.data(stationNames)
	.enter().append("text")
	.attr("class", "stationName")
	.attr("id", function(d, i) {return i-1})
	.text(function(d) {return d})
	.on("mouseover", function(d, i) {
		svg.selectAll(".bar")
			.data(station_data[i])
			.enter().append("rect")
	    	.attr("class", "bar")
   			.attr("x", function(d) { return x(d[0]); })
    		.attr("width", x.rangeBand())
   			.attr("y", function(d) { return y(d[1]); })
    		.attr("height", function(d) { return height - y(d[1]); });
	});