//_______Lists to Chart
var allTotBikes = [];
var timeStamps = [];

//_________CITIBIKE4
var time = citibike4["executionTime"];
var stations = citibike4["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike4["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE5
var time = citibike5["executionTime"];
var stations = citibike5["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike5["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE6
var time = citibike6["executionTime"];
var stations = citibike6["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike6["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE7
var time = citibike7["executionTime"];
var stations = citibike7["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike7["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE8
var time = citibike8["executionTime"];
var stations = citibike8["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike8["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE9
var time = citibike9["executionTime"];
var stations = citibike9["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike9["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

//_________CITIBIKE10
var time = citibike10["executionTime"];
var stations = citibike10["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike10["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);


//_________CITIBIKE11
var time = citibike11["executionTime"];
var stations = citibike11["stationBeanList"];
numStations = stations.length;

//Loop through the stations in the list, find the # available bikes and add to running total of available bikes for the stations in this list (from time0
var i = 0;
var totBikes = 0
while (i<numStations){
    var numBikes = (citibike11["stationBeanList"][i]).availableBikes;
    totBikes = numBikes + totBikes;
    i = i + 1;
    };
//Append the total to the list of total bikes & times that will be used in chart
allTotBikes.push(totBikes);
timeStamps.push(time);

j = 0 
data = []
while (j<allTotBikes.length){
    data[j] ={"label":timeStamps[j],"value":allTotBikes[j]};
    j = j + 1;
};


    //maximum of data you want to use
    var data_max = 6000,

    //number of tickmarks to use
    num_ticks = 5,

    //margins
    left_margin = 60,
    right_margin = 60,
    top_margin = 30,
    bottom_margin = 0;


    var w = 500,                        //width
        h = 500,                        //height
        color = function(id) { return '#00b3dc' };

    var x = d3.scale.linear()
        .domain([0, data_max])
        .range([0, w - ( left_margin + right_margin ) ]),
        y = d3.scale.ordinal()
        .domain(d3.range(data.length))
        .rangeBands([bottom_margin, h - top_margin], .5);


    var chart_top = h - y.rangeBand()/2 - top_margin;
    var chart_bottom = bottom_margin + y.rangeBand()/2;
    var chart_left = left_margin;
    var chart_right = w - right_margin;

    /*
     *  Setup the SVG element and position it
     */
    var vis = d3.select("body")
        .append("svg:svg")
            .attr("width", w)
            .attr("height", h)
        .append("svg:g")
            .attr("id", "barchart")
            .attr("class", "barchart")


    //Ticks
    var rules = vis.selectAll("g.rule")
        .data(x.ticks(num_ticks))
    .enter()
        .append("svg:g")
        .attr("transform", function(d)
                {
                return "translate(" + (chart_left + x(d)) + ")";});
    rules.append("svg:line")
        .attr("class", "tick")
        .attr("y1", chart_top)
        .attr("y2", chart_top + 4)
        .attr("stroke", "black");

    rules.append("svg:text")
        .attr("class", "tick_label")
        .attr("text-anchor", "middle")
        .attr("y", chart_top)
        .text(function(d)
        {
        return d;
        });
    var bbox = vis.selectAll(".tick_label").node().getBBox();
    vis.selectAll(".tick_label")
    .attr("transform", function(d)
            {
            return "translate(0," + (bbox.height) + ")";
            });

    var bars = vis.selectAll("g.bar")
        .data(data)
    .enter()
        .append("svg:g")
            .attr("class", "bar")
            .attr("transform", function(d, i) { 
                    return "translate(0, " + y(i) + ")"; });

    bars.append("svg:rect")
        .attr("x", right_margin)
        .attr("width", function(d) {
                return (x(d.value));
                })
        .attr("height", y.rangeBand())
        .attr("fill", color(0))
        .attr("stroke", color(0));


    //Labels
    var labels = vis.selectAll("g.bar")
        .append("svg:text")
            .attr("class", "label")
            .attr("x", 0)
            .attr("text-anchor", "right")
            .text(function(d) {
                    return d.label;
                    });

    var bbox = labels.node().getBBox();
    vis.selectAll(".label")
        .attr("transform", function(d) {
                return "translate(0, " + (y.rangeBand()/2 + bbox.height/4) + ")";
                });

labels = vis.selectAll("g.bar").append("svg:text")
        .attr("class", "value")
        .attr("x", function(d)
                {
                return x(d.value) + right_margin + 10;
                })
        .attr("text-anchor", "left")
        .text(function(d)
        {
        return "" + d.value;
        });

    bbox = labels.node().getBBox();
    vis.selectAll(".value")
        .attr("transform", function(d)
        {
            return "translate(0, " + (y.rangeBand()/2 + bbox.height/4) + ")";
        });

    //Axes
    vis.append("svg:line")
        .attr("class", "axes")
        .attr("x1", chart_left)
        .attr("x2", chart_left)
        .attr("y1", chart_bottom)
        .attr("y2", chart_top)
        .attr("stroke", "black");
     vis.append("svg:line")
        .attr("class", "axes")
        .attr("x1", chart_left)
        .attr("x2", chart_right)
        .attr("y1", chart_top)
        .attr("y2", chart_top)
        .attr("stroke", "black");
