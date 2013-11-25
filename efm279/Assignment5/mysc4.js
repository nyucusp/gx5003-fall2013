{
    var container=new Array();
    var totalbike=new Array();
    var sname=new Array();
    var sid=new Array();
    var reqtime=new Array();
    var dota = new Array();
    j=0
    
    var jxhr = [];
    urls=['bike1.json','bike2.json','bike3.json','bike4.json','bike5.json','bike6.json']
    var f = function(data) {
            totalbike[j]=0;
            reqtime[j]=0;
            sid
            container[0]=new Array();
            container[0].push('Station Name');
            container[0].push('Available Bikes');
            container[0].push('Status Value');
            
            reqtime[j]=data.executionTime;
        var count=1;    
            container[count]=new Array();
        for (var i in data.stationBeanList) {
            count=count+1;
            totalbike[j]=totalbike[j]+data.stationBeanList[i].availableBikes;
            sname[j]=sname[j]+data.stationBeanList[i].stationName+ '<br>';
            sid[j]=sid[j]+data.stationBeanList[i].id;
         }
       
       // alert(totalbike[j])
       // alert(reqtime[j])
        dota[j.toString()]=totalbike[j];
            
       j=j+1;   
  }
 
      
    $.getJSON(urls[0], f)
    $.getJSON(urls[1], f)
    $.getJSON(urls[2], f)
    $.getJSON(urls[3], f)
    $.getJSON(urls[4], f)
    $.getJSON(urls[5], f)
        
   
    for (var i in sname){
      document.getElementById("div2").innerHTML=sid[i]+sname[i]+ '<br>';  
        
    } 
    
   //alert(totalbike)
  // alert(reqtime[j])
  // alert(dota['0']);
   

   
   var width = 100,
    height = 600;

var x = d3.scale.linear()
      .domain([0, 1])
      .range([50, width+50]);
  
var y = d3.scale.linear()
    .domain([ 0,6000])
    .range([height,0]);

var chart = d3.select("body").append("svg")
     .attr("class", "chart")
     .attr("width", width* dota.length - 1)
     .attr("height", height)
 //   .data(totalbike);

chart.selectAll("rect")
     .data(dota)
   .enter().append("rect")
     .attr("x", function(d, i) { return x(i) - .5; })
     .attr("y", function(d, i) { return y(d); })
     .attr("width", width)
     .attr("height", function(d,i) { return height-y(d); })
    
            
  chart.selectAll("text")
     .data(dota)
   .enter().append("text")
     .attr("x", function(d,i) { return x(i) +50; })
     .attr("y", height+20 )
     .attr("dy", ".35em")
     .text(function(d,i) { return reqtime[i].substring(12,22); });
        
  chart.append("line")
     .attr("x1", 50)
     .attr("x2", 50+width * dota.length)
     .attr("y1", height - .5)
     .attr("y2", height - .5)
     .style("stroke", "#000");   
     

     var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");
    
    
  chart.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + width*0.4 + ",0)")
      .call(yAxis)
      .append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", -45)
    
    .attr("dy", ".71em")
    .style("text-anchor", "end")
    .text("Total Number of Available Bikes")
 //     .ticks(10, "%");



}