#!/usr/bin/node

const request = require('request');
const movieId = parseInt(process.argv[2]);
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (err, response, body) => {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    for (let i = 0; i < content.results.length; i++) {
      if (content.results[i].episode_id === movieId) {
        const characterUrls = content.results[i].characters;

        function processCharacter (error, response, body) {
          if (response.statusCode === 200) {
            const character = JSON.parse(body);
            console.log(character.name);
          } else {
            console.log(error);
          }
          const index = characterUrls.indexOf(response.request.uri.href);
          if (index > -1) {
            characterUrls.splice(index, 1);
          }
          if (characterUrls.length === 0) {
            process.exit(0);
          }
        }
        for (const characterUrl of characterUrls) {
          request.get(characterUrl, processCharacter);
        }
      }
    }
  } else {
    console.log(err);
  }
});
