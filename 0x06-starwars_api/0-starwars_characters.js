#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  function aRequest (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        resolve(JSON.parse(body));
      });
    });
  }

  async function main () {
    const movieId = process.argv[2];
    const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
    let characters = '';
    let movie;
    try {
      movie = await aRequest(movieUrl);
    } catch (error) {
      console.error(error);
    }
    characters = movie.characters;
    for (const character of characters) {
      const details = await aRequest(character);
      console.log(details.name);
    }
  }
  main();
}
