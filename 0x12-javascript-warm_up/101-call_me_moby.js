#!/usr/bin/node
module.exports.callMeMoby = function (x, aFunc) {
  for (let i = 0; i < x; i++) {
    aFunc();
  }
};
