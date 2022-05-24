#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request.get(url, (err, response, body) => {
  if (err) console.log(err);
  const chars = JSON.parse(body).characters;
  chars.forEach((char, index) => {
    request.get(char, (err, resp, body) => {
      if (err) console.log(err);
      console.log(JSON.parse(body).name);
    });
  });
});
