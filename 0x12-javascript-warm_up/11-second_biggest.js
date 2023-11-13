#!/usr/bin/node
const numbers = process.argv.slice(2);
let SecBig = 0;

if (numbers.length > 1) {
  numbers.sort();
  SecBig = numbers[numbers.length - 2];
}
console.log(SecBig);
