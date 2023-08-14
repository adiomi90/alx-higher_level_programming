#!/usr/bin/node

// Prints a number

const myInt = parseInt(process.argv[2]);

if (myInt) {
  console.log('My number: ' + myInt);
} else {
  console.log('Not a number');
}
