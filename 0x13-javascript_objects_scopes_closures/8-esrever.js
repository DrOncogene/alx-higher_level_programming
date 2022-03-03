#!/usr/bin/node
module.exports.esrever = (list) => {
  const revList = [];
  for (let i = 0; i < list.length; i++) {
    revList.unshift(list[i]);
  }
  return revList;
};
