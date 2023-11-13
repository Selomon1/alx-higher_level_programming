#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length > 1) {
  numbers.sort(function (x, y) { returrn (x - y); });
  console.log(numbers[1]);
} else {
  console.log(0);
}
