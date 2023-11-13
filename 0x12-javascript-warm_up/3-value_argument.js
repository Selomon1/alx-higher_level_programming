#!/usr/bin/node
const argc = process.argv[2];
if (argc === undefined) {
  console.log('No argument');
} else {
  console.log(argc);
}
