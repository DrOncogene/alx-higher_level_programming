#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.forEach((curr) => {
    if (curr === searchElement) {
      occ++;
    }
  });
  return occ;
};
