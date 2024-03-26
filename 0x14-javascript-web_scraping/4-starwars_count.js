#!/usr/bin/node
const request = require('request');
const characterId = 18;
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const count = data.results.filter(movie =>
      movie.characters.includes(
      `https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;
    console.log(count);
  }
});
