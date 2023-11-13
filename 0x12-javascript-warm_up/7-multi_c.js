#!/usr/bin/node

// script print x times of first argument

const firstArg = parseInt(process.argv[2]);

if firstArg {
  for (let i = 0; i < firstArg; i++) {
    console.log('C is fun');
  }
} else {
  console.log("Missing number of occurrences");
}

