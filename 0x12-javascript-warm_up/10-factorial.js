#!/usr/bin/node
function factorial (a) {
  if (a <= 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
if (process.argv.length === 2) {
  console.log(1);
} else {
  if (Number.isInteger(Number(process.argv[2]))) {
    const a = Number(process.argv[2]);
    console.log(factorial(a));
  } else {
    console.log('Not an integer');
  }
}
