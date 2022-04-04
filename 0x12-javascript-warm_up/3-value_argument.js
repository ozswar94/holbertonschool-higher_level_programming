#!/usr/bin/node

let len = 0;

process.argv.forEach(() => {
  len++;
});

if (len === 2) {
  console.log('No argument');
} else {
  process.argv.forEach((val, index) => {
    if (index > 1) {
      console.log(`${val}`);
    }
  });
}
