#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request.get(url, 'utf-8', (error, response, body) => {
  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  } else {
    console.log(error);
  }
});
