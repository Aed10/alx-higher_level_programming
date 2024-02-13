#!/usr/bin/node
let max = 0;

for (let i = 2; i < process.argv.length; i++) {
  const arg = Number(process.argv[i]);

  if (arg > max) {
    max = arg;
  }
}

console.log(max);
