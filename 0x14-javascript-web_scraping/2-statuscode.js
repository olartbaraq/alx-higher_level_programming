#!/usr/bin/node

const request = require('request');
const firstArgument = process.argv[2];
const siteAddress = String(firstArgument);
request(siteAddress, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: %i', response.statusCode);
});
