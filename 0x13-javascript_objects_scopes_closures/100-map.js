#!/usr/bin/node

const thisList = require('./100-data.js').list;
const newList = thisList.map((x, index) => x * index);

console.log(thisList);
console.log(newList);
