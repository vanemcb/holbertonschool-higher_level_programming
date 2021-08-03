#!/usr/bin/node
const newList = require('./100-data.js');
const multList = newList.list.map((num, index) => num * index);
console.log(newList.list);
console.log(multList);
