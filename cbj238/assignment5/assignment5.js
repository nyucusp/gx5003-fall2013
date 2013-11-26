var jsonData = new Array(json0, json1, json2, json3, json4, json5, json6, json8, json9, json10, json11, json12, json13, json14, json15, json16, json17, json18, json19);
var stationData = getStationList();
var dataLabels = Array();

var margin = {top: 20, right: 30, bottom: 100, left: 40},
        width = 600 - margin.left - margin.right,
        height = 550 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

function getAvailableBikes(jsonObject, stationID) {
    var total = 0;
    for (var station in jsonObject["stationBeanList"]) {
        var thisStation = jsonObject.stationBeanList[station];
        if (stationID === -1 || stationID === thisStation.id) {
                total += thisStation.availableBikes;
        }
    }
    return total;
}

function getAvailableBikesOverTime(stationID) {
    var timeArray = new Array();
    for (var i=0; i < jsonData.length; i++) {
        timeArray.push( {"time" : jsonData[i].executionTime, "bikes" : getAvailableBikes(jsonData[i], stationID)} );
    }
    return timeArray;
}

function getStationList() {
    // We assume that the stations never change, and therefore only loop through the first to get the station names.
    var stationArray = new Array();
    for (var i=0; i < jsonData[0].stationBeanList.length; i++) {
        var stationptr = jsonData[0].stationBeanList[i];
        stationArray.push( {"id" : stationptr.id, "name":stationptr.stationName} );
    }
    return stationArray;
}

function getTicksFromRange(range) {
    if (range < 3)
        return 2;
    else if (range < 20)
        return Math.round(range);
    else if (range < 50)
        return Math.round(range / 2);
    else
        return Math.round(range / 10);
}

function drawBikesBarGraph(stationID){
    d3.select("#chart1").selectAll("g").remove();

    var data = getAvailableBikesOverTime(stationID);

    var min = d3.min(data, function(d) {return d.bikes; });
    var max =d3.max(data, function(d) {return d.bikes; })
    var ticks = getTicksFromRange(max - min);
    yAxis.ticks(ticks);

    x.domain(data.map(function(d) { return d.time; }));
    if (stationID===-1) {
        y.domain([min *.995, max]);
    } else {
        var maxMod = 0;
        var minMod = 0;
        if ((max - min) < 3)
        {
            maxMod = 1;
            minMod = 1;
        }

        y.domain([min-minMod, max+maxMod]);
    }
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
            .attr("dy", ".4em")
            .style("text-anchor", "end")
            .text("Available Bikes");

    var bar = bikeChart.selectAll(".bar")
        .data(data);

    bar.enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.time); })
        .attr("y", function(d) { return y(d.bikes); })
        .attr("height", function(d) { return height - y(d.bikes); })
        .attr("width", x.rangeBand());

    // Remove old elements as needed
    bar.exit().remove();
}

function drawStations() {
    // Now load the station names into the second div stationlist
    d3.select("#stationlist")
        .selectAll("div")
        .data(stationData)
        .enter().append("div")
            .attr("class", "station")
            .text(function(d) { return d.name; })
            .on('mouseover', function(d){
                d3.select(this).style({color:'red'});
                drawBikesBarGraph( d.id );
            })
            .on('mouseout', function(d){
                d3.select(this).style({color:'purple'});
                drawBikesBarGraph(-1);
            });
}

window.onload=function() {

    drawBikesBarGraph(-1);
    drawStations();
}

