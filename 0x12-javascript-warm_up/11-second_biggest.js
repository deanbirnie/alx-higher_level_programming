#!/usr/bin/node

const [, , ...args] = process.argv;

function findSecondLargest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  numbers = numbers.map(Number);
  numbers.sort((a, b) => b - a);

  return numbers[1];
}

const secondLargest = findSecondLargest(args);
console.log(secondLargest);
