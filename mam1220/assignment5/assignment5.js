//*************************************************************************
// Citybike Data Handling JavaScript
// Java Script
//
// November 2013
//
// By: Michael Musick
//
//*************************************************************************

var numOfStations;
var stationLocations = new Array();
var numOfSamples;
var bikeData = new Array();
var sampledHours = new Array();
var currentStation = 0;   
var bData = [];

function loadPage() {
	// $('div#test').text(bike1);
	
	bikeData[0] = bike1;
	bikeData[1] = bike2;
	bikeData[2] = bike3;
	bikeData[3] = bike4;
	bikeData[4] = bike5;
	bikeData[5] = bike6;

	// get the number of stations
	numOfSamples = bikeData.length;
	// $('div#test').text(numOfSamples);
	
	// get the times sampled
	for(var i = 0; i < numOfSamples; i++) {
		sampledHours[i] = bikeData[i].executionTime;
		item = {};
		item.timestamp = bikeData[i].executionTime;
		item.bikesAvailable = 0;
		bData[i] = item;
	}

	// get the location names
	for(var i = 0; i< bike1.stationBeanList.length; i++ ) {
		stationLocations[i] = bike1.stationBeanList[i].stationName;
	}
	numOfStations = stationLocations.length;

	buildGraph( currentStation );

	buildInteractiveText();


}

function buildInteractiveText() {

	d3.select(".textArea").append("p").text("New paragraph!");

}




function buildGraph( station ) {
	// $('div#test').text(stationLocations);	

	for( var i=0; i<numOfSamples; i++ ) {
		bData[i].bikesAvailable = Number(bikeData[i].stationBeanList[station].availableBikes);
	}

	// var data = numOfBikesAvailable;
	// $('div#test').text(bData);	


	var margin = {top: 20, right: 30, bottom: 30, left: 40},
	    width = 960 - margin.left - margin.right,
	    height = 500 - margin.top - margin.bottom;

	var y = d3.scale.linear()
		.range([height, 0]);

	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width], .1);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");


	var chart = d3.select(".chart")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


	
	y.domain([0, d3.max(bData, function(d) { return d.bikesAvailable; })]);
	x.domain(bData.map(function(d) { return d.timestamp; }));

	chart.append("g")
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis)


	chart.append("g")
	      .attr("class", "y axis")
	      .call(yAxis)
	    .append("text")
	      .attr("transform", "rotate(-90)")
	      .attr("y", 6)
	      .attr("dy", ".71em")
	      .style("text-anchor", "end")
	      .text("Number of Bikes Available");

	chart.selectAll(".bar")
	  .data(bData)
	.enter().append("rect")
	  .attr("class", "bar")
	  .attr("x", function(d) { return x(d.timestamp); })
	  .attr("y", function(d) { return y(d.bikesAvailable); })
	  .attr("height", function(d) { return height - y(d.bikesAvailable); })
	  .attr("width", x.rangeBand());





}



