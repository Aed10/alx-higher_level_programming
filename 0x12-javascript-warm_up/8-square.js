#!/usr/bin/node
if (process.argv.length === 2) {
    console.log('Missing size');
} else {
    if (Number.isFinite(Number(process.argv[2]))) {
        const numberOfOccurrences = Math.round(Number(process.argv[2]));

        for (let i = 0; i < numberOfOccurrences; i++) {
            let row = '';
            for (let j = 0; j < numberOfOccurrences; j++) { row += 'X'; }
            console.log(row);
        }
    } else {
        console.log('Missing size');
    }
}
