#!/usr/bin/node

const fs = require('fs');
const argvs = process.argv[2];
const content = process.argv[3];
const fileName = argvs;
const pathFile = String(fileName);
const contents = String(content);

fs.writeFile(pathFile, contents, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
