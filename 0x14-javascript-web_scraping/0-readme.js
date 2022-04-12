#!/usr/bin/node

const argvs = process.argv.slice(2);
file_path = String(argvs);
const fs = require('fs');

fs.readFile( file_path, 'utf-8', (error, data) => {
    if (error) {
	console.log(error);
	return;
    }

    console.log(data.toString());
});
