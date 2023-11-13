#!/usr/bin/node
const x = parseInt(process.argv[2]);
let loop = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (loop = 0; loop < x; loop++) {
    console.log('C is fun');
  }
}
