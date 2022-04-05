#!/usr/bin/node
const myDict = require('./101-data').dict;

const keys = {};
for (const key in myDict) {
  const value = myDict[key];
  if (!keys[value]) { keys[value] = []; }
  keys[value].push(key);
}
console.log(keys);
