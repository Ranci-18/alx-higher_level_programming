#!/usr/bin/node
let i;

if (!isNaN(Number(process.argv[2]))) {
  for (i = 0; i < Number.parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
