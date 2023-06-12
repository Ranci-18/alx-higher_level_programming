#!/usr/bin/node
let i;
let j;
let row;

if (!isNaN(Number(process.argv[2]))) {
  for (i = 0; i < Number.parseInt(process.argv[2]); i++) {
    row = '';
    for (j = 0; j < Number.parseInt(process.argv[2]); j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
