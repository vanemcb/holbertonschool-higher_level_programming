#!/usr/bin/node
let varString1;
let varString2;
if (typeof process.argv[2] === 'undefined') {
  varString1 = 'undefined';
} else {
  varString1 = process.argv[2];
}
if (typeof process.argv[3] === 'undefined') {
  varString2 = 'undefined';
} else {
  varString2 = process.argv[3];
}
console.log(varString1, 'is', varString2);
