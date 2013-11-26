var jsonData = new Array(json0, json1, json2, json3, json4, json5, json6, json8, json9, json10, json11, json12, json13, json14, json15, json16, json17, json18, json19);
var availableBikes = getAvailableBikesOverTime();

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .domain([0, d3.max(availableBikes)])
    .range([0, width], .1)

var y = d3.scale.linear()
    .range( [height, 0] )

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks(10, "%")

// var svg = d3.select("body").append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom )
//     .append("g")
//     .attr("transform", "translate("+margin.left + "," + margin.top + ")");

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

function getData() {
    x.domain(data.map(function(d) { return }));
}

window.onload=function() {
    // d3.select("#div1").selectAll("div")
    //         .data(availableBikes)
    //     .enter().append("div")
    //         .style("width", function(d) { return x(d["bikes"]) + "px"; })
    //     .text(function(d) { return d["time"]; })

    var chart = d3.select("#div1")
        .attr("width", width)
        .attr("height", height)

    var bar = chart.selectAll("g")
        .data(availableBikes)
    .enter().append("g")
        .attr("transform", function(d, i) { return "translate(0," + i * height + ")"; });

    bar.append("rect")
        .attr("width", x)
        .attr("height", height-1);

    bar.append("text")
        .attr("x", function(d) { return x(d) - 3; })
        .attr("y", height / 2)
        .attr("dy", ".35em")
        .text(function(d) { return d; });
}

