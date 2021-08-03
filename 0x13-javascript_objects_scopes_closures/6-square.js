#!/usr/bin/node

/* Class Square that defines a square and inherits from Rectangle */

class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
