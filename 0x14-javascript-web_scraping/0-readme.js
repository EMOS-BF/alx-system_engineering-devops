#!/usr/bin/node
const fs = require('fs');
fs.readfile(process.arg[2], 'utf-8', function(err, content){
	if (err){
	    console.log(err);
	}else {
	    process.stdout.write(content);
	}
});
