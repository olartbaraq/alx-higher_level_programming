#!/usr/bin/node

const request = require('request');
const urlArgs = process.argv[2];
const realUrl = String(urlArgs);

request(realUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const todosArray = JSON.parse(body);
  const key = {};
  for (let i = 0; i < todosArray.length; i++) {
    const idJson = (todosArray[i]).userId;
    if ((todosArray[i]).completed) {
      if (key[String(idJson)]) {
        key[String(idJson)] += 1;
      } else {
        key[String(idJson)] = 1;
      }
    }
  }
  console.log(key);
});
