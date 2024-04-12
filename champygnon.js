const csv = require('csv-parser');
const fs = require('fs')

const csvPath = 'champignons.csv';

let champignons = [];
let shapes = [];
let surfaces = [];

function loadCSVData() {
    return new Promise((resolve, reject) => {
        fs.createReadStream(csvPath)
            .pipe(csv())
            .on('data', (data) => {
                champignons.push(data);
            })
            .on('end', () => {
                shapes = getShapes(champignons);
                surfaces = getSurfaces(champignons);
                shapes.sort();
                surfaces.sort();
                //console.log(shapes, surfaces);
                resolve({ shapes, surfaces });
            })
            .on('error', (error) => {
                reject(error);
            });
        });
}

function getShapes(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleShapes = new Set(champignons.map(objet => objet.Shape));

    // Convertir l'ensemble en une liste
    return [...ensembleShapes];
}

function getSurfaces(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleSurfaces = new Set(champignons.map(objet => objet.Surfaces));

    // Convertir l'ensemble en une liste
    return [...ensembleSurfaces];
}

// Exporter les données récupérées dans le CSV
module.exports = loadCSVData;