#!/usr/bin/node

const occurence = parseInt(process.argv[2]);

if (!occurence) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occurence; i++) {
    console.log('C is fun');
  }
}
