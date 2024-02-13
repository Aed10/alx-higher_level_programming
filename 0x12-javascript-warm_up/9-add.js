#!/usr/bin/node
/**
 * Adds two numbers together
 * @param {number} a - the first number
 * @param {number} b - the second number
 * @returns {number} the sum of a and b
 */
function add (a, b) {
  return a + b;
}
const a = process.argv[2];
const b = process.argv[3];

console.log(add(a, b));
