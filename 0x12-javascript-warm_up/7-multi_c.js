#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined ||
    isNaN(myArgs[0])) {
  console.log('Missing number of occurrences');
} else {
  const strConvert = parseInt(myArgs[0]);
  for (let item = 0; item < strConvert; item++) {
    console.log('C is fun');
  }
}
