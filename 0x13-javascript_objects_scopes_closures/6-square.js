#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
      return;
    }
    super.print(c);
  }
}

module.exports = Square;
