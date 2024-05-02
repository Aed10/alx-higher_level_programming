#!/usr/bin/node
// Read a  file

const fs = require('fs');

// Read the file
const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
