#!/usr/bin/node
function add (a, b) {
  console.log(Number.parseInt(process.argv[2]) + Number.parseInt(process.argv[3]));
}

add();
