#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined ||
    isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  const strConvert = parseInt(myArgs[0]);
  for (let sqr1 = 0; sqr1 < strConvert; sqr1++) {
    console.log('X'.repeat(strConvert));
  }
}
