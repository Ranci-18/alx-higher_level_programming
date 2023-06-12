#!/usr/bin/node
const args = process.argv;
let largest = 0;
let secondLargest = -Infinity;
let i;

if (args.length === 2) {
  console.log(0);
} else if (args.length === 3) {
  console.log(1);
} else {
  for (i = 2; i < args.length; i++) {
    if (Number.parseInt(args[i]) > largest) {
      secondLargest = largest;
      largest = Number.parseInt(args[i]);
    } else if (Number.parseInt(args[i]) < largest && Number.parseInt(args[i]) > secondLargest) {
      secondLargest = Number.parseInt(args[i]);
    }
  }

  if (secondLargest === -Infinity) {
    console.log(0);
  } else {
    console.log(secondLargest);
  }
}
