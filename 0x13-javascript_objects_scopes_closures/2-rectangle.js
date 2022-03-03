#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || (typeof h || typeof w) === 'undefined') {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
