	//get the data
	var stations=bike["stationlist"];
	function getdata(stationname)
	{
		stationname = typeof stationname !== 'undefined' ? stationname : "All Stations";
		var targetstation;
		
		for(var i in stations)
		{ 
			if(stations[i]["stationname"]==stationname)
			{
				targetstation=stations[i]["hourlist"];
			}
		}

		counts=[];data=[];hourstr=[];
		for(var i in targetstation)
		{
			data.push(i)
			hourstr.push(targetstation[i]["hour"]+":00");
			counts.push(targetstation[i]["Available"]);
		}

		return [data,hourstr,counts,stationname];
	};

	//get hours and counts

	function draw(data,counts,hourstr,stationname)
	{
	//set the margin		
	var margin = {top: 40, right: 40, bottom: 50, left: 160},
		width = 560 - margin.left - margin.right,
		height = 320 - margin.top - margin.bottom;
	
	//set the x scale as ordinal
	var x = d3.scale.ordinal()
		.rangeRoundBands([0, width],.1);
		
	x.domain(data.map(function(data) { return hourstr[data]; }));
	//var x = d3.scale.linear()
	//	.range([0, width]);
	
	//set y scale as linear
	var y = d3.scale.linear()
		.range([height, 0]);
	y.domain([0, d3.max(counts)]);	
	//set the xAsis
	var xAxis = d3.svg.axis()
		.scale(x)
		.orient("bottom");

	//set the yAsis
	var yAxis = d3.svg.axis()
		.scale(y)
		.orient("left")
		
	//append a p with a svg inside to draw stuff
	var element = document.getElementById("thechart");
	//alert(element);
	if(element!==null)
	{element.parentNode.removeChild(element);}
	
	var svg = d3.select("#div1")
	.append("p").attr("id","thechart").append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	  .append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
		
	svg.append("g")//draw the title
	  .attr("x", 0)
	  .attr("y",0)
	  .append("text")
	  .attr("x",100)
	  .attr("y",-10)
	  .attr("fontsize",30)
	  .text(stationname);
  

	svg.append("g")//draw the x axis
	  .attr("class", "x axis")
	  .attr("transform", "translate(0," + height + ")")
	  .call(xAxis)
	  .append("text")
	  .attr("y", 40)
	  .attr("x", 150)
	  .attr("fontsize",10)
	  .text("Time");
  
	svg.append("g")//draw the y axis
	 .attr("class", "y axis")
	 .call(yAxis)
	.append("text")
	  .attr("transform", "rotate(-90)")
	  .attr("y", -60)
	  .attr("x",-60)
	  .attr("fontsize",10)
	  .attr("dy", "0.7em")
	  .style("text-anchor", "end")
	  .text("Available Bikes");

	svg.selectAll(".bar")//draw bars
	  .data(data)
	.enter().append("rect")
	  .attr("class", "bar")
	  .attr("x", function(data){return x(hourstr[data])+1;})
	  .attr("width", function(data){return 50;})
	  .attr("y",function(data) {return y(counts[data]); })
	  .attr("height", function(data) { return height - y(counts[data]); });
	}
	
	result=getdata();
	data=result[0];hourstr=result[1];counts=result[2],title=result[3];
	draw(data,counts,hourstr,title);
	//div2
	stationnamelist=["All Stations"];
	for(var i in stations)
	{ 
		
		if(stations[i]["stationname"]!=="All Stations")
		{
			stationnamelist.push(stations[i]["stationname"])
		}
	}
	
	var stationp = d3.select("#div2").selectAll(".stationtext")
	.data(stationnamelist)
	.enter().append("h")
	.attr("onmouseover","getid(this);")
	.attr("id",function(data){return data;}).append("text").text(" | ")
	.append("text").attr("class","stationtext")
	.text(function(data){return data;});
	
	//hover
	var HoverListener = {
		addElem: function( elem, callback, delay )
		{
			if ( delay === undefined )
			{
				delay = 50;
			}

			var hoverTimer;

			addEvent( elem, 'mouseover', function()
				{hoverTimer = setTimeout( callback, delay );} 
			);

			addEvent( elem, 'mouseout', function()
				{clearTimeout( hoverTimer );} 
			);
		}
	}



	//  Generic event abstractor
	function addEvent(obj, evt, fn )
	{
		if ( 'undefined' != typeof obj.addEventListener )
		{
			obj.addEventListener( evt, fn, false );
		}
		else if ( 'undefined' != typeof obj.attachEvent )
		{
			obj.attachEvent( "on" + evt, fn );
		}
	}

	var idlist=[];
	
	function getid(obj){id=obj.id;};
	
	addEvent( window, 'load', function(){
		for(var i in stationnamelist)
		{

			id=stationnamelist[i];
			idlist.push(id);
			HoverListener.addElem(
			document.getElementById( id )
			, function(){
			result=getdata(id);
			data=result[0];hourstr=result[1];counts=result[2];
			draw(data,counts,hourstr,id);
			
			} );			
		}
		}
		);	

	


	