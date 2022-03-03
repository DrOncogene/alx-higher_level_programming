#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || (typeof h || typeof w) === 'undefined') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += 'X';
      }
      console.log(rect);
    }
  }
}

module.exports = Rectangle;
