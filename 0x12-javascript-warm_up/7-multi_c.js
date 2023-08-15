#!/usr/bin/node

const [, , x] = process.argv;
const convertedArg = parseInt(x);
let i;

if (!isNaN(convertedArg)) {
    for (i = 0; i < convertedArg; i++) {
	console.log('C is fun');
    }
} else {
    console.log('Missing number of occurrences');
}
