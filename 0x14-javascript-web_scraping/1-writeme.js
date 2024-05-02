#!/usr/bin/node

const fs = require('fs');

// Write to a file
const file = process.argv[2];
const content = process.argv[3];
fs.writeFile(file, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
