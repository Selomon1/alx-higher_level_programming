#!/usr/bin/node
let priN = 0;
exports.logMe = function (item) {
  console.log(priN + ': ' + item);
  priN++;
};
