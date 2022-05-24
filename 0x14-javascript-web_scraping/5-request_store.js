#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request.get(url, (err, response, body) => {
  if (err) console.log(err);
  fs.open(file, 'w', (err, fd) => {
    if (err) console.log(err);
    fs.write(fd, body, 'utf8', (err) => {
      if (err) console.log(err);
    });

    fs.close(fd, (err) => {
      if (err) console.log(err);
    });
  });
});
