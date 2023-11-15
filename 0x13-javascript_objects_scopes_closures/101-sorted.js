#!/usr/bin/node
const Odict = require('./101-data.js').dict;
let Ndict = {};
for (let key in Odict) {
  if (Ndict[Odict[key]] === undefined) {
    Ndict[Odict[key]] = [key];
  } else {
    Ndict[Odict[key]].push(key);
  }
}
console.log(Ndict);
