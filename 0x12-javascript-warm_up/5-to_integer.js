#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else if (!Number(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.round(Number(process.argv[2])));
}
