#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (err, response, body) => {
  if (err) console.log(err);
  const todos = JSON.parse(body);
  const completed = {};
  todos.forEach((todo, index) => {
    if (todo.completed) {
      todo.userId in completed
        ? completed[todo.userId]++
        : completed[todo.userId] = 1;
    }
  });
  console.log(completed);
});
