#!/usr/bin/node
exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0; i < list.length / 2; i++) {
    [list[j], list[i]] = [list[i], list[j]];
    j -= 1;
  }
  return list;
};
