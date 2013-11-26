var json1 = {
	'transform': function(json,transform,_options) {
		//create the default output
		var out = {'events':[],'html':''};
		//Make sure if there is a transform & json object
		if( transform !== undefined || json !== undefined ) {
			//Normalize strings to JSON objects if necessary
			var obj = typeof json === 'string' ? JSON.parse(json) : json;	
			//Transform the object (using the options)
			out = json1._transform(obj, transform, options);
		}
	},
	//Get the html value of the object
	'_getValue':function(obj, transform, key,index) {
		
		var out = '';
		var val = transform[key];
		var type = typeof val;
		
		if (type === 'function') {
			return(val.call(obj,obj,index));
		} else if (type === 'string') break;
						}
					}