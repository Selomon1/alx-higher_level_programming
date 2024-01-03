#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const charId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter(film =>
      film.characters.find(character => character.endsWith(`/${charId}/`))
    ).length;
    console.log(count);
  }
});
