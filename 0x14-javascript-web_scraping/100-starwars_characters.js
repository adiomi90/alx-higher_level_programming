#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, content) => {
  if (!error) {
    const characters = JSON.parse(content).characters;
    characters.forEach(character => {
      request(character, (err, resp, content) => {
        if (!err) {
          const name = JSON.parse(content).name;
          console.log(name);
        }
      });
    });
  }
});
