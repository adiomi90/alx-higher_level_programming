#!/usr/bin/node

// Prints first elemnt without using length

const myVar = process.argv[2];
if (myVar === undefined) {
  console.log('No argument');
} else {
  console.log(myVar);
}

#!/usr/bin/node

// Prints the first argument passed to it

const myArgs = process.argv[2];
if (myArgs === undefined) {
  console.log('No argument');
} else {
  console.log(myArgs);
}
