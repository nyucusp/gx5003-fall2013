var jsonData = new Array(json0, json1, json2, json3, json4, json5, json6, json8, json9, json10, json11, json12, json13, json14, json15, json16, json17, json18, json19);
var data = getAvailableBikesOverTime();
var dataLabels = Array();

var margin = {top: 20, right: 30, bottom: 100, left: 40},
    width = 600 - margin.left - margin.right,
    height = 550 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0])
    .domain([d3.min(data, function(d) {return d.bikes; }) *.995, d3.max(data, function(d) {return d.bikes; })]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10);

function getAvailableBikes(jsonObject) {
    var total = 0;
    for (var station in jsonObject["stationBeanList"]) {
        total += jsonObject["stationBeanList"][station]["availableBikes"];
    }
    return total;
}

function getAvailableBikesOverTime() {
    var timeArray = new Array();
    for (var i=0; i < jsonData.length; i++) {
        timeArray.push( {"time" : jsonData[i].executionTime, "bikes" : getAvailableBikes(jsonData[i])} );
    }
    return timeArray;
}

window.onload=function() {
    x.domain(data.map(function(d) { return d.time; }));

    var bikeChart = d3.select("#chart1")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", "translate(" + margin.left + ", " + margin.top + ")")

    bikeChart.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", ".15em")
            .attr("transform", function(d) {
                return "rotate (-65)"
            });

    bikeChart.append("g")
            .attr("class", "y axis")
            .call(yAxis)
        .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("Available Bikes");

    var bar = bikeChart.selectAll(".bar")
        .data(data)
    .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.time); })
        .attr("y", function(d) { return y(d.bikes); })
        .attr("height", function(d) { return height - y(d.bikes); })
        .attr("width", x.rangeBand());
}

