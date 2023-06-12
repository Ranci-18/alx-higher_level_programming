#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const num = Number.parseInt(process.argv[2]);
const fin = factorial(num);
console.log(fin);
