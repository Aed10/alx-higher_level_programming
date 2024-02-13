#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  if (Number.isFinite(Number(process.argv[2]))) {
    const numberOfOccurrences = Math.round(Number(process.argv[2]));
    for (let i = 0; i < numberOfOccurrences; i++) { console.log('C is fun'); }
  }
}
