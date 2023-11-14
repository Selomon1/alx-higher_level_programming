#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
	  if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
		  return;
	  }
	  this.width = w;
	  this.height = h;
  }

  print () {
	  let loop = 0;
	  while (loop < this.height) {
		  console.log('X'.repeat(this.width));
		  loop++;
	  }
  }
};
