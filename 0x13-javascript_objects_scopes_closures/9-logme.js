#!/usr/bin/node
/* Function that prints the number of arguments already printed and the
new argument value */

let cont = 0;

exports.logMe = function (item) {
  console.log(cont + ': ' + item);
  cont++;
};
