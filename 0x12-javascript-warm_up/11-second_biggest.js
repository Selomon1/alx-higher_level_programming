#!/usr/bin/node
let SecBig = 0;
const numbers = process.argv.slice(2);

if (numbers.length > 1) {
  numbers.sort();
  SecBig = numbers[numbers.length - 2];
}
console.log(SecBig);
