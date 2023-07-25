#!/usr/bin/node

const request = require('request');
const characterIdUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < content.results.length; i++) {
      if (content.results[i].characters.includes(characterIdUrl)) { count += 1; }
    }
    console.log(count);
  }
});
