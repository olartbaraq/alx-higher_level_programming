#!/usr/bin/node

const argvs = process.argv.slice(2);
const filePath = String(argvs);
const fs = require('fs');

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(data.toString());
});
