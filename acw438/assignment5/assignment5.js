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

var highest_y = 0;
var avail_tot_bikes = new Array();
var labar = ['03:03pm', '06:16pm', '08:32pm', '08:52pm', '10:53pm', '11:14pm']

console.log('should be first');

for (i=1; i<7; i++) 
{
     var filename = "bike" + i + ".json"
		
     d3.json(filename, function(json) {
     	console.log(filename + ' ' + json["executionTime"]);


     	var station_num = json.stationBeanList.length;
     	var avail_bike_list = new Array();
     	for (var i=0; i<station_num; i++) {
     		avail_bike_list.push(json.stationBeanList[i].availableBikes);
     		};

		console.log(d3.sum(json.stationBeanList, function(station) {
				return station.availableBikes;
			}));

		var tot_val = d3.sum(avail_bike_list);
		console.log(tot_val);
		avail_tot_bikes.push(tot_val);
		tot_val > highest_y ? highest_y = tot_val: 1==1;
		
		console.log('should be middle');
		
		x.domain(labar);

		
		svg.append("g")
    .attr("class", "y axis")
    .call(yAxis)

svg.selectAll(".bar")
    .data(avail_tot_bikes)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d, i) { return x(labar[i]); })
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d); })
    .attr("height", function(d) { return height - y(d); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

svg.append("g")
    .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Available Bikes");

})
};

console.log('should be last');
y.domain([0, 5500]);