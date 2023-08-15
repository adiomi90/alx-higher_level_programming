#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  list.forEach(item => item === searchElement && count++);
  return count;
}
