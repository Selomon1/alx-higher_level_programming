#!/usr/bin/node
const squ = parseInt(process.argv[2]);
let loop = 0;

if (isNaN(squ)) {
  console.log('Missing size');
} else {
  for (loop = 0; loop < squ; loop++) {
    console.log('X'.repeat(squ));
  }
}
