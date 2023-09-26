#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  try {
    const movie = JSON.parse(body);
    movie.characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        }

        try {
          const character = JSON.parse(body);
          console.log(character.name);
        } catch (e) {
          console.error(e);
        }
      });
    });
  } catch (er) {
    console.error(er);
  }
});
