#!/usr/bin/node

const request = require('request');
const argument = process.argv[2];
const siteAddress = String(argument);
const options = {
  url: siteAddress,
  headers: {
    'User-agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    const filtered = info.results;
    // console.log(filtered);
    let count = 0;
    // since fitered is now an array of dictionary(json)
    for (let i = 0; i < filtered.length; i++) {
      const results = filtered[i];
      const characters = results.characters;
      // console.log(characters);
      for (let j = 0; j < characters.length; j++) {
        if ((characters[j]).includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
}
request(options, callback);
