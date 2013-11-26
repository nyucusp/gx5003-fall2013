var w = 700;
var h = 400;
var margin = 90;


var url = "bike.json";
var url2 = "bike2.json";
var url3 = "bike3.json";
var url4 = "bike4.json";
var url5 = "bike5.json";
var url6 = "bike6.json";
var url7 = "bike7.json";



function update(s,svg){
d3.json(url, function (data) {
    d3.json(url2, function (data2) {
        d3.json(url3, function (data3) {
            d3.json(url4, function (data4) {
                d3.json(url5, function (data5) {
                    d3.json(url6, function (data6) {
                        d3.json(url7, function (data7) {
d3.selectAll("g").remove();
d3.selectAll("rect").remove();
d3.selectAll("text").remove();


                            var a = data.executionTime;
                            var b = data2.executionTime;
                            var c = data3.executionTime;
                            var d = data4.executionTime;
                            var e = data5.executionTime;
                            var f = data6.executionTime;
                            var g = data7.executionTime;
                            data = data.stationBeanList
                            data2 = data2.stationBeanList
                            data3 = data3.stationBeanList
                            data4 = data4.stationBeanList
                            data5 = data5.stationBeanList
                            data6 = data6.stationBeanList
                            data7 = data7.stationBeanList


  
  var numOfBikes = 0;
		var numOfBikes2 = 0;
		var numOfBikes3 = 0;
		var numOfBikes4 = 0;
		var numOfBikes5 = 0;
		var numOfBikes6 = 0;
		var numOfBikes7 = 0;
			for (var i=0;i<data.length;i++){ 
		numOfBikes += data[i].availableBikes
		numOfBikes2 += data2[i].availableBikes
		numOfBikes3 += data3[i].availableBikes
		numOfBikes4 += data4[i].availableBikes
		numOfBikes5 += data5[i].availableBikes
		numOfBikes6 += data6[i].availableBikes
		numOfBikes7 += data7[i].availableBikes
		};
     
	 if(s<401){
                            var dataset = [
								{ key: new Date("2013-11-22 03:00:03 PM"), value: "0"}, 
								{ key: new Date(a),value: data[s].availableBikes}, 
								{ key: new Date(b),value: data2[s].availableBikes}, 
								{ key: new Date(c),value: data3[s].availableBikes}, 
								{ key: new Date(d),value: data4[s].availableBikes}, 
								{ key: new Date(e),value: data5[s].availableBikes}, 
								{ key: new Date(f),value: data6[s].availableBikes}, 
								{ key: new Date(g),value: data7[s].availableBikes}, 
                                { key: new Date("2013-11-22 10:45:03 PM"),value: "0"}
								];

	 }
	 else{
		 var dataset = [
								{ key: new Date("2013-11-22 03:00:03 PM"), value: "0"}, 
								{ key: new Date(a),value: numOfBikes}, 
								{ key: new Date(b),value: numOfBikes2}, 
								{ key: new Date(c),value: numOfBikes3}, 
								{ key: new Date(d),value: numOfBikes4}, 
								{ key: new Date(e),value: numOfBikes5}, 
								{ key: new Date(f),value: numOfBikes6}, 
								{ key: new Date(g),value: numOfBikes7}, 
                                { key: new Date("2013-11-22 10:45:03 PM"),value: "0"}
								];
		 };


                            var key = function (d) {
                                return d.key;
                            };

                            var value = function (d) {
                                return d.value;
                            };
							
							var maximum = d3.max(dataset, function(d) {return d.value;});

                            var x_domain = d3.extent(dataset, function (d) {
                                return d.key;
                            }),
                                y_domain = d3.extent(dataset, function (d) {
                                    return d.value;
                                });

                            var date_format = d3.time.format("%b/%d %H:%M");




  
/*
Coded by Abdullah Kurkcu
 */
 
                            // define the y scale  (vertical)
                            var yScale = d3.scale.linear()
                                .domain([0, maximum + maximum/2]).nice() // make axis end in round number
                            .range([h - margin, margin]); // map these to the chart height, less margin.  In this case 300 and 100
                            //REMEMBER: y axis range has the bigger number first because the y value of zero is at the top of chart and increases as you go down.


                            var xScale = d3.time.scale()
                                .domain(x_domain) // values between for month of january
                            .range([90, 700]); // map these sides of the chart, in this case 100 and 600

                  
                            // define the y axis
                            var yAxis = d3.svg.axis()
                                .orient("left")
                                .scale(yScale);

                            // define the x axis
                            var xAxis = d3.svg.axis()
                                .orient("bottom")
                                .scale(xScale)
                                .tickFormat(date_format)
                                .ticks(5);

                            // draw y axis with labels and move in from the size by the amount of margin
                            svg.append("g")
                                .attr("class", "axis")
                                .attr("transform", "translate(" + margin + ",0)")
                                .call(yAxis);

                            // draw x axis with labels and move to the bottom of the chart area
			    console.log("Coded by Abdullah Kurkcu");
                            svg.append("g")
                                .attr("class", "xaxis axis") // two classes, one for css formatting, one for selection below
                            .attr("transform", "translate(0," + (h - margin) + ")")
                                .call(xAxis);


                            //Create bars
                            svg.selectAll("rect")
                                .data(dataset)
                                .enter()
                                .append("rect")
                                .attr("x", function (d) {
                                return (xScale(d.key));
                            })
                                .attr("y", function (d) {
                                return yScale(d.value);

                            })
                                .attr("width", (w - margin) / (dataset.length * 2))
                                .attr("height", function (d) {
                                return h - margin - yScale(d.value);
                            })
                                .attr("fill", function (d) {
                                return "rgb(96, 0, " + (d.value * 10) + ")";
                            })

                            //Tooltip
                            .on("mouseover", function (d) {
                                //Get this bar's x/y values, then augment for the tooltip
                                var xPosition = parseFloat(d3.select(this).attr("x"));
                                var yPosition = parseFloat(d3.select(this).attr("y")) + 14;

                                //Update Tooltip Position & value
                                d3.select("#tooltip")
                                    .style("left", xPosition + "px")
                                    .style("top", yPosition + "px")
                                    .select("#value")
                                    .text(d.value);
                                d3.select("#tooltip").classed("hidden", false)
                            })
                                .on("mouseout", function () {
                                //Remove the tooltip
                                d3.select("#tooltip").classed("hidden", true);
                            });


                            svg.selectAll("text")
                                .data(dataset,key)
                                .enter()
                                .append("text")
                                .text(function (d) {
                                return d.value;
                            })
                                .attr("text-anchor", "middle")
                                .attr("x", function (d) {
                                return xScale(d.key)+15;
								
                            })
                                .attr("y", function (d) {
                                return yScale(d.value) + 25;
                            })
                                .attr("font-family", "sans-serif")
                                .attr("font-size", "11px")
                                .attr("fill", "white");

                            svg.selectAll(".xaxis text") // select all the text elements for the xaxis
                            .attr("transform", function (d) {
                                return "translate(" + this.getBBox().height * -2 + "," + this.getBBox().height + ")rotate(-30)";
                            });
							
		


                            svg.append("text")
                                .attr("text-anchor", "middle") // this makes it easy to centre the text as the transform is applied to the anchor
                            .attr("transform", "translate(" + (w / 2) + "," + (h - (margin / 3)) + ")") // centre below axis
                            .text("Time of Day");

                            svg.append("text")
                                .attr("text-anchor", "middle") // this makes it easy to centre the text as the transform is applied to the anchor
                            .attr("transform", "translate(" + (margin / 2) + "," + (h / 2) + ")rotate(-90)") // text is drawn off the screen top left, move down and out and rotate
                        	   .text("The Number of Available Bikes");
		
							

                        });
                    });
                });
            });
        });
    });
});
}



d3.json(url, function (data2) {
var aq = data2.stationBeanList;
var stations2= [];
for (var i=0;i<aq.length;i++)
{stations2.push(aq[i].stationName)}

                            // create an svg container
var svg = d3.select("body").select("#div1")
    .append("svg")
    .attr("width", w)
    .attr("height", h);
update(401,svg);


toplist = d3.select("#div2").append("ul");
toplist.selectAll("li")
    .data(stations2)
    .enter()
    .append("li")
    .text(function(d){return d;})
	.on("mouseover", function(d,i){return update(i,svg);})
});



// JavaScript Document