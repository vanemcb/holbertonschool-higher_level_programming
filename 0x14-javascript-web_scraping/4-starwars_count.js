#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const movies = JSON.parse(body).results;

  let count = 0;

  for (const movie of movies) {
    for (const char of movie.characters) {
      if (char.endsWith('18/') === true) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
