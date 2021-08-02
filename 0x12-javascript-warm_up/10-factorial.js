#!/usr/bin/node
function fact (num) {
  if (!num) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(fact(num));
