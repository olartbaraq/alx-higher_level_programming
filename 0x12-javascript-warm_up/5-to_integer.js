#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (myArgs[0] === undefined) {
  console.log('Not a number');
} else {
  const newNumber = parseInt(myArgs[0]);
  if (isNaN(newNumber)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + newNumber);
  }
}
