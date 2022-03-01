#!/usr/bin/node

function factorial (number) {
  if (number <= 1 ||
      isNaN(number)) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const myArgs = process.argv.slice(2);

const num = parseInt(myArgs[0]);

console.log(factorial(num));
