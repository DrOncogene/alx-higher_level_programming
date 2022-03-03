#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
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
