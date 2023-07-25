#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request.get(url, (err, response, body) => {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    console.log(content.title);
  } else {
    console.log(err);
  }
});
