#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const url = `https://swapi.dev/api/films/${Id}/`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const character of characters) {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }
  }
});
