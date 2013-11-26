
var time1 = citibike1.executionTime;
var availableBikes = (citibike1["stationBeanList"][0]).availableBikes;

//alert(time1);
//alert(availableBikes);


len = (citibike1["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes1 = 0;
while (i<len) 
{
var availableBikes = (citibike1["stationBeanList"][i]).availableBikes;
totalBikes1 = totalBikes1 + availableBikes;
i = i + 1;
};
//alert(totalBikes1);
//alert("Bike 1 Done");



//CITIBIKE 2                            
var time2 = citibike2.executionTime;
var availableBikes2 = (citibike2["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes2);

len2 = (citibike2["stationBeanList"]).length;
//alert(len2);

var i = 0;
var totalBikes2 = 0;
while (i<len2) 
{
var availableBikes2 = (citibike2["stationBeanList"][i]).availableBikes;
totalBikes2 = totalBikes2 + availableBikes2;
i = i + 1;
};
//alert(totalBikes2);
//alert("Bike 2 Done");






//CITIBIKE 3                            
var time3 = citibike3.executionTime;
var availableBikes = (citibike3["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike3["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes3 = 0;
while (i<len) 
{
var availableBikes = (citibike3["stationBeanList"][i]).availableBikes;
totalBikes3 = totalBikes3 + availableBikes;
i = i + 1;
};
//alert(totalBikes3);
//alert("Bike 3 Done");



//CITIBIKE 4                            
var time4 = citibike4.executionTime;
var availableBikes = (citibike4["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike4["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes4 = 0;
while (i<len) 
{
var availableBikes = (citibike4["stationBeanList"][i]).availableBikes;
totalBikes4 = totalBikes4 + availableBikes;
i = i + 1;
};

//alert(totalBikes4);
//alert("Bike 4 Done");



//CITIBIKE 5                            
var time5 = citibike5.executionTime;
var availableBikes = (citibike5["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike5["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes5 = 0;
while (i<len) 
{
var availableBikes = (citibike5["stationBeanList"][i]).availableBikes;
totalBikes5 = totalBikes5 + availableBikes;
i = i + 1;
};

//alert(totalBikes5);
//alert("Bike 5 Done");

//CITIBIKE 6                            
var time6 = citibike6.executionTime;
var availableBikes = (citibike6["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike6["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes6 = 0;
while (i<len) 
{
var availableBikes = (citibike6["stationBeanList"][i]).availableBikes;
totalBikes6 = totalBikes6 + availableBikes;
i = i + 1;
};
//alert(totalBikes6);
//alert("Bike 6 Done");

//CITIBIKE 7                            
var time7 = citibike7.executionTime;
var availableBikes = (citibike7["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike7["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes7 = 0;
while (i<len) 
{
var availableBikes = (citibike7["stationBeanList"][i]).availableBikes;
totalBikes7 = totalBikes7 + availableBikes;
i = i + 1;
};
//alert(totalBikes7);
//alert("Bike 7 Done");

//CITIBIKE 8                            
var time8 = citibike8.executionTime;
var availableBikes = (citibike8["stationBeanList"][0]).availableBikes;
//alert(time);
//alert(availableBikes);

len = (citibike8["stationBeanList"]).length;
//alert(len);

var i = 0;
var totalBikes8 = 0;
while (i<len) 
{
var availableBikes = (citibike8["stationBeanList"][i]).availableBikes;
totalBikes8 = totalBikes8 + availableBikes;
i = i + 1;
};
//alert(totalBikes8);
alert("Bike 8 Done");


    
    // Create Global Variable
    var dataset;

    dataset = [
    {CustomerCount: totalBikes1, State: time1},
    {CustomerCount: totalBikes2, State: time2},
    {CustomerCount: totalBikes3, State: time2},
    {CustomerCount: totalBikes4, State: time4},
    {CustomerCount: totalBikes5, State: time5},
    {CustomerCount: totalBikes6, State: time6},
    {CustomerCount: totalBikes7, State: time7},
    {CustomerCount: totalBikes8, State: time8},
    ]

      // Call function
      Graph(dataset);
      

    // Create function
    function Graph(input) {
    
    // Declare Variables
    var margin = {top: 60, right: 60, bottom: 60, left:120},
    w = 600 - margin.left - margin.right,
    h = 400 - margin.top - margin.bottom;
    
    //Create X Scale for bar graph
    var xScale = d3.scale.ordinal()
               .domain(input.map(function (d){ return d.State;}))
               .rangeRoundBands([0, w], 0.05);
    
    //Create Y Scale for bar graph
    var yScale = d3.scale.linear()
             .domain([0,d3.max(input, function(d) { return d.CustomerCount; })])
             .range([h, 0]);
  
    //Create X Axis 
    var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient("bottom");
                   
    //Create Y Axis
    var yAxis = d3.svg.axis()
            .scale(yScale)
            .orient('left');
    
    //Create SVG element
    var svg = d3.select("body")
          .append("svg")
          .attr("width", w + margin.left + margin.right)
          .attr("height", h + margin.top + margin.bottom)
          .append('g')
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
          
    //Create X axis 
    svg.append("g")
       .attr("class", "axis x")
       .attr("transform", "translate(0," + h + ")")
       .call(xAxis);
            
    //Create Title 
    svg.append("text")
    .attr("x", w / 2 )
        .attr("y", 0)
        .style("text-anchor", "middle")
        .text("Citi Bike Availability");
       
    //Create X axis label   
    svg.append("text")
    .attr("x", w / 2 )
        .attr("y",  h + margin.bottom)
        .style("text-anchor", "middle")
        .text("Timestamps");
          
    //Create Y axis
    svg.append("g")
       .attr("class", "axis y")
       .call(yAxis);
       
    //Create Y axis label
    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0-margin.left)
        .attr("x",0 - (h / 2))
        .attr("dy", "1em")
        .style("text-anchor", "middle")
        .text("Availability");
          
    //Add rectangles
    svg.selectAll(".bar")
       .data(input)
       .enter()
       .append("rect")
       .attr("class", "bar")
           .style("fill", "cyan")
       .attr("x", function(d) { return xScale(d.State); })
       .attr("y", function(d) { return yScale(d.CustomerCount) })
       .attr("width", xScale.rangeBand()) //returns rangeRoundBands width
       .attr("height", function(d) { return h - yScale(d.CustomerCount) });
//    document.getElementById("div1").innerHTML = svg;


    }; // end Graph function


alert('end');



