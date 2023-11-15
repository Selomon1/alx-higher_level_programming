#!/usr/bin/node
const fs = require('fs');
const firstA = fs.readFileSync(process.argv[2], 'utf8');
const secondA = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], firstA + secondA);
