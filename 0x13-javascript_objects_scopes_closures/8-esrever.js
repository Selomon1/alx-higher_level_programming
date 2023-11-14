#!/usr/bin/node
exports.esrever = function (list) {
  const newL = [];
  let loop = 0;
  for (loop = 0; loop < list.length; loop++) {
    newL.unshift(list[loop]);
  }
  return newL;
};
