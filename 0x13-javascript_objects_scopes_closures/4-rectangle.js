#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || (typeof h || typeof w) === 'undefined') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print (c='X') {
    for (let i = 0; i < this.height; i++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += c;
      }
      console.log(rect);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
