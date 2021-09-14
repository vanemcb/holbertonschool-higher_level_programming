#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }

  const users = JSON.parse(body);
  const dict = {};

  for (let i = 1; i <= 10; i++) {
    let count = 0;
    for (const us of users) {
      if (us.userId === i && us.completed === true) { count++; }
    }
    dict[i] = count;
  }
  console.log(dict);
});
