#!/usr/bin/node
let max = 0;
const list = [];
if (process.argv.length === 2 || process.argv.length === 3) {
  max = 0;
} else {
  for (let i = 2; i < process.argv.length; i++) {
    const arg = Number(process.argv[i]);
    list.push(arg); // ajouter tous les arguments à la liste
  }
  list.sort((a, b) => b - a); // trier la liste par ordre décroissant
  max = list[1]; // accéder au deuxième élément
}

console.log(max);
