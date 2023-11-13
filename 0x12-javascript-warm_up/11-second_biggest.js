#!/usr/bin/node
const numbers = process.argv.slice(2);

if (numbers.length > 1) {
  numbers.sort(function (num1, num2) { return (num2 - num1); });
  console.log(numbers[1]);
} else {
  console.log(0);
}
