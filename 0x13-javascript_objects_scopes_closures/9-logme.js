#!/usr/bin/node
module.exports.logMe = function (item) {
  let index = 0;
  function inner (item=item) {
    console.log(index++ + ': ' + item);
  }
  return inner;
}();
