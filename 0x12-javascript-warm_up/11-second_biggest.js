#!/usr/bin/node

if (process.argv.length <= 4) {
  console.log(0);
} else {
  const tab = [];
  process.argv.forEach(function (items) {
    if (Number(items)) { tab.push(Number(items)); }
  });

  tab.sort();
  console.log(tab[tab.length - 2]);
}
