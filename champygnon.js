const csv = require('csv-parser');
const fs = require('fs')

const csvPath = 'champignons.csv';

let champignons = [];
let shapes = [];
let surfaces = [];

console.log("Start champygnon.js");

// On récupère les informations du CSV
fs.createReadStream(csvPath)
  .pipe(csv())
  .on('data', (data) => {
      champignons.push(data);
  })
  .on('end', () => {
    //console.log(champignons);
    shapes = getShapes(champignons);
    surfaces = getSurfaces(champignons);
    shapes.sort();
    surfaces.sort();
});

//console.log("After readstream");

//console.log(champignons);
//console.log(shapes);
//console.log(surfaces);

function getShapes(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleShapes = new Set(champignons.map(objet => objet.Shape));

    return [...ensembleShapes];
}

function getSurfaces(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleSurfaces = new Set(champignons.map(objet => objet.Surfaces));

    // Convertir l'ensemble en une liste
    return [...ensembleSurfaces];
}

console.log("End champygnon.js");
console.log(shapes);
console.log(surfaces);
module.exports = {shapes, surfaces};