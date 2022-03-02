#!/usr/bin/node
module.exports.addMeMaybe = function (num, theFunc) {
  theFunc(++num);
};
