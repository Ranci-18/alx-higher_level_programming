#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};

for (const key in dict) {
  if (dict[key]) {
    const val = dict[key];
    if (newDict[val]) {
      newDict[val].push(key);
    } else {
      newDict[val] = [key];
    }
  }
}
console.log(newDict);
