#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
