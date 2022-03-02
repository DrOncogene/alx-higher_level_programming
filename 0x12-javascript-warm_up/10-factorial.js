#!/usr/bin/node
const num = parseInt(process.argv[2]);
console.log(factorial(num));

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
}
