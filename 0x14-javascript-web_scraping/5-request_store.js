#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const urlArgs = process.argv[2];
const realUrl = String(urlArgs);
const fileArgs = process.argv[3];
const realPath = String(fileArgs);

request(realUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(realPath, body, 'utf-8', error => {
    if (error) {
      console.log(error);
    }
  });
});
