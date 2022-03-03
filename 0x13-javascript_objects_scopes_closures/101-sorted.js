#!/usr/bin/node
const dict = require('./101-data').dict;

const occurrences = [];
for (const key in dict) {
  if (occurrences.includes(dict[key])) {
    continue;
  }
  occurrences.push(dict[key]);
}

const newDict = {};

for (const occ of occurrences) {
  const ids = [];
  for (const [key, value] of Object.entries(dict)) {
    if (occ === value) {
      ids.push(key);
    }
  }
  newDict[occ] = ids;
}
console.log(newDict);
