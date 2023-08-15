#!/usr/bin/node

let firstArg;
let secondArg;

if (process.argv[2]) {
  firstArg = process.argv[2];
}
if (process.argv[3]) {
  secondArg = process.argv[3];
}

console.log(`${firstArg} is ${secondArg}`);
