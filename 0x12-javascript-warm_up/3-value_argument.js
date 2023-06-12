#!/usr/bin/node
const args = process.argv;
const numArgs = args.length - 2;

if (numArgs === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
