#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterID = '18';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes(characterID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
