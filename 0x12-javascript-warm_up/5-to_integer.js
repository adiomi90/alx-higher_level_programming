#!/usr/bin/node

// prints first argument converted to int

const firstArg = parseInt(process.argv[2]);
if (firstArg) {
  console.log('My number: ' + firstArg);
} else {
  console.log('Not a number');
}
