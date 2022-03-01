#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let item = 0; item < list.length; item++) {
    if (list[item] === searchElement) {
      count++;
    }
  }
  return count;
};
