#!/usr/bin/node
const fs = require('fs');

let data = fs.readFileSync(process.argv[2], 'utf8');
data += fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], data);
