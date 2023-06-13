#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const data1 = fs.readFileSync(fileA, {encoding: 'utf-8'});
const data2 = fs.readFileSync(fileB, {encoding: 'utf-8'});
fs.writeFileSync(fileC, data1 + data2, {encoding: 'utf-8'});
