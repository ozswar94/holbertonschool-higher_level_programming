#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurenceElement = 0;

  list.forEach(function (items) {
    if (items === searchElement) { occurenceElement++; }
  });
  return occurenceElement;
};
