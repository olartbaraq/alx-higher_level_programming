#!/usr/bin/node

const myArgs = process.argv.slice(2);
if (myArgs.length === 2) {
  console.log(myArgs[0] + ' is ' + myArgs[1]);
} else if (myArgs.length === 1) {
  console.log(myArgs[0] + ' is ' + myArgs[1]);
} else {
  console.log(myArgs[0] + ' is ' + myArgs[1]);
}
