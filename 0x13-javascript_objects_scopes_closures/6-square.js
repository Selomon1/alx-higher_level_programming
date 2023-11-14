#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    for (let loop = 0; loop < this.height; loop++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
};
