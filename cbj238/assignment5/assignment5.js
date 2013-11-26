var jsonData = new Array(json0, json1, json2, json3, json4, json5, json6, json8, json9, json10, json11, json12, json13, json14, json15, json16, json17, json18, json19);
var data = getAvailableBikesOverTime();
var dataLabels = Array();
for (var i=0; i < data.length; i++) {
    dataLabels.push(data[i].time);
}

var margin = {top: 20, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .domain(dataLabels)
    .rangeBands([0, width])

var y = d3.scale.linear()
    .range([height, 0])
    .domain([0, d3.max(data, function(d) {return d.bikes; })]);

var barWidth = width / data.length;

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
    var bikeChart = d3.select("#chart1")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", "translate(" + margin.left + ", " + margin.top + ")");

    var bar = bikeChart.selectAll("g")
        .data(data)
    .enter().append("g")
        .attr("transform", function(d, i) { return "translate(" + i * barWidth + ",0)"; });

    bar.append("rect")
        .attr("y", function(d) { return y(d.bikes); })
        .attr("height", function(d) { return height - y(d.bikes); })
        .attr("width", barWidth - 1);

    bar.append("text")
        .attr("x", barWidth / 2)
        .attr("y", function(d) { return y(d.bikes) + 3; })
        .attr("dy", ".75em")
        .text(function(d) { return d.bikes; });
}

