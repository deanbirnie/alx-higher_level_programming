#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function getCharacterName (characterUrls, index = 0) {
  if (index >= characterUrls.length) return;

  const characterUrl = characterUrls[index];
  request.get(characterUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    }

    try {
      const character = JSON.parse(body);
      console.log(character.name);
      getCharacterName(characterUrls, index + 1);
    } catch (e) {
      console.error(e);
    }
  });
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  try {
    const movie = JSON.parse(body);
    getCharacterName(movie.characters);
  } catch (e) {
    console.error(e);
  }
});
