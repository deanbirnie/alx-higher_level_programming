#!/usr/bin/node

let firstArg;

if (process.argv[2]) {
  firstArg = process.argv[2];
  console.log(firstArg);
} else {
  console.log('No argument');
}
