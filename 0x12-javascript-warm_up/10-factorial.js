#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  n = parseInt(n);

  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const [, , arg] = process.argv;
const num = parseInt(arg);

const result = factorial(num);
console.log(result);
