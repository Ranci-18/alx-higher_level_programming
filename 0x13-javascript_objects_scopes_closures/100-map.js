#!/usr/bin/node

const { list } = require('./100-data');
console.log(list);

const newList = list.map((val, idx) => val * idx);
console.log(newList);
