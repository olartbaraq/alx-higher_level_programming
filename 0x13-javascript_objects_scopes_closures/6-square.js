#!/usr/bin/node

const PrevSquare = require('./5-square');
module.exports = class Square extends PrevSquare {
  charPrint (c) {
    if (c === undefined) {
	c = 'X';
    }
    for (let item = 0; item < this.height; item++) {
	console.log(c.repeat(this.width));
    }
  }
};
