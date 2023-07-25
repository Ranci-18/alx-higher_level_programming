#!/usr/bin/node

const reqst = require('request');
const url = process.argv[2];
reqst.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
