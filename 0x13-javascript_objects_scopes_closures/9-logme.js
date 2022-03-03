#!/usr/bin/node
module.exports.logMe = function (item) {
  if (typeof this.index === 'undefined') {
    this.index = 0;
  }
  console.log(this.index++ + ': ' + item);
};
