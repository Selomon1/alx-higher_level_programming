#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    charactersUrls.forEach(charUrl => {
      request(charUrl, (charError, charRespo, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const charData = JSON.parse(charBody);
          console.log(charData.name);
        }
      });
    });
  }
});
