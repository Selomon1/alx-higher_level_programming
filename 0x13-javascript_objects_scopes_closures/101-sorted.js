#!/usr/bin/node
const Odict = require('./101-data.js').dict;
const Ndict = {};
for (const key in Odict) {
  if (Ndict[Odict[key]] === undefined) {
    Ndict[Odict[key]] = [key];
  } else {
    Ndict[Odict[key]].push(key);
  }
}
console.log(Ndict);
