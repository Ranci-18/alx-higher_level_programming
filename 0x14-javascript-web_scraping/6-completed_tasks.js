#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < content.length; i++) {
      if (content[i].completed === true) {
        if (content[i].userId in completed) {
          completed[content[i].userId] += 1;
        } else {
          completed[content[i].userId] = 1;
        }
      }
    }
    console.log(completed);
  } else {
    console.log(err);
  }
});
