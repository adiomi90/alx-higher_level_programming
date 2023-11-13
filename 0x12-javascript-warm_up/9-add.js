#!/usr/bin/node

// add two integers using arguments

const a = intParse(process.argv[2]);
const b = intParse(process.argv[3]);

function add(a, b) {
  return a + b;
}

console.log(add(a, b));
