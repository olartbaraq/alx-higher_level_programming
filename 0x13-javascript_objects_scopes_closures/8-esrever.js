#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let item = list.length - 1; item >= 0; item--) {
    reverseList.push(list[item]);
  }
  return reverseList;
};
