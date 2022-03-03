#!/usr/bin/node
module.exports.converter = function (base) {
  return function (num) {
    if (base === 10) {
      return num;
    }
    return num.toString(base);
  };
};
