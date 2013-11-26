    // Define Margin and SVG height & width
    var margin = {top:50, right:50, bottom: 150, left: 150},
        width  = 500 - margin.left - margin.right,
        z = d3.scale.category20c(),
        height = 500 - margin.top  - margin.bottom;

    // Define number format for y axis
    var formatComma = d3.format(",");

    // Define ordinal scale for x axis
    var xScale = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1);

    // Define linear scale for y axis
    var yScale = d3.scale.linear()
        .range([height, 0]);

    // Define X Axis
    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient("bottom");

    // Define Y Axis
    var yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left")
        .tickFormat(function(d) { return "$" + formatComma(d); });

    // Define Innter Drawing Space
    var innerDrawingSpace = d3.select("#div2").append("svg")
        .attr("width",  width  + margin.left + margin.right )
        .attr("height", height + margin.top  + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Get JSON Data
    d3.json("citibike1.json", function(error, data) {

      // Add H1 Element With Actor Name
      d3.select("#div1").append("h1")
          .text("Citibike Available Stations");

      // Set the X Scale Domain
      xScale.domain(data.stationBeanList.map(function(d) { return d.id }));

      // Set the Y Scale Domain
      yScale.domain([0, d3.max(data.movies, function(d) { return d.availableBikes; })]).nice();

      // Create the X Axis, Move it to the bottom and transform the axis text
      innerDrawingSpace.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0," + height + ")")
          .call(xAxis)
          .selectAll("text")
              .style("text-anchor", "end")
              .attr("dx", "-0.5em")
              .attr("dy", ".5em")
              .attr("transform", function(d) { return "rotate(-55)"; })

      // Create the Y Axis, Move it to the bottom and transform the axis text
      innerDrawingSpace.append("g")
          .attr("class", "y axis")
          .call(yAxis);
      
      // Create the bars
      innerDrawingSpace.append("g").attr("class", "bars")
          .selectAll(".bar")
          .data(data.stationBeanList)
        .enter().append("rect")
          .attr("class", "bar")
          .attr("x", function(d) { return xScale(d.id);   })
          .attr("y", function(d) { return yScale(d.availableBikes); })
          .attr("width", xScale.rangeBand())
          .attr("height", function(d) { return height - yScale(d.availableBikes); })
          .style("fill", "steelblue");
      
      // Add Basic Mouse Over Div
      var div = d3.select("body").append("div")
          .style("position", "absolute")
          .style("text-align", "center")
          .style("width", "240px;")
          .style("height", "3.5em")
          .style("font", "1.5em sans-serif")
          .style("color", "yellow")
          .style("background", "#001A33")
          .style("border", "solid 1px #001A33")
          .style("border-radius", "8px")
          .style("pointer-events", "none")
          .style("opacity", 0);

      //  Mouse Over Function
      function mouseOver(d) {
        div.html("Station Name:<br />" + d.stationBeanList.stationName + " " + "<br />Status: " + d.stationBeanList.statusValue)
            .style("left" , (d3.event.pageX - 120) + "px")
            .style("top", (d3.event.pageY) + "px")
            .style("opacity", 1);
      }

      // Mouse Out Function
      function mouseOut(d) {
        div.style("opacity", 1e-6);
      }

      // Add Mouse Over / Mouse Out Functionality
      d3.selectAll(".bar")
          .on("mouseover", mouseOver)
          .on("mouseout" , mouseOut );

    });