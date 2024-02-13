#!/usr/bin/node
let max = 0;
const list = [];
if (process.argv.length === 2) {
  max = 0;
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const arg = Number(process.argv[i]);

    if (arg > max) {
      max = arg;
      list.push(max);
    }
  }
  max = list.slice(-2, -1)[0];
}

console.log(max);
