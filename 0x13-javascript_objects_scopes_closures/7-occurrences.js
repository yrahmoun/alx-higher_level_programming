#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const e in list) {
    if (list[e] === searchElement) count++;
  }
  return count;
};
