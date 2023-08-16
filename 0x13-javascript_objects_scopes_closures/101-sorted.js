#!/usr/bin/node
const inputDictionary = require('./101-data').dict;

const outputDictionary = {};

for (const key in inputDictionary) {
  const ocurrence = inputDictionary[key];
  outputDictionary[ocurrence] = [];
  for (const keys in inputDictionary) {
    if (inputDictionary[keys] === ocurrence) {
      outputDictionary[ocurrence].push(keys);
    }
  }
}
console.log(outputDictionary)
