#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) console.log(err);
  const films = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < films.length; i++) {
    const chars = films[i].characters;
    for (let j = 0; j < chars.length; j++) {
      const id = chars[j].substr(-3, 2);
      if (id === '18') count++;
    }
  }
  console.log(count);
});
