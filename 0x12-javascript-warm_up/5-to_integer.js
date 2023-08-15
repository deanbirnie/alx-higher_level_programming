#!/usr/bin/node

const [, , firstArg] = process.argv;
const convertedArg = parseInt(firstArg);

if (!isNaN(convertedArg)) {
  console.log(`My number: ${convertedArg}`);
} else {
  console.log('Not a number');
}
