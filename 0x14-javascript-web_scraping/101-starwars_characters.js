#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

(async () => {
  try {
    const movieData = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) reject(error);
        else resolve(JSON.parse(body));
      });
    });

    for (const charUrl of movieData.characters) {
      const charData = await new Promise((resolve, reject) => {
        request(charUrl, (charError, charRespo, charBody) => {
          if (charError) reject(charError);
          else resolve(JSON.parse(charBody));
        });
      });
      console.log(charData.name);
    }
  } catch (err) {
    console.error(err);
  }
})();
