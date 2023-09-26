#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const wedgeId = '18';

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }

  try {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(wedgeId)) {
          count += 1;
        }
      });
    });

    console.log(count);
  } catch (e) {
    console.error(e);
  }
});
