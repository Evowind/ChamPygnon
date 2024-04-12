const csv = require('csv-parser');
const fs = require('fs')

const csvPath = 'champignons.csv';

let champignons = [];
let shapes = [];
let surfaces = [];

// Récupérer les données CSV
function loadCSVData() {
    // La fonction est asynchrone donc on renvoie une promesse
    return new Promise((resolve, reject) => {
        fs.createReadStream(csvPath)
            .pipe(csv())
            .on('data', (data) => {
                champignons.push(data);
            })
            .on('end', () => {
                shapes = getShapes(champignons);
                surfaces = getSurfaces(champignons);
                shapes.sort().shift();
                surfaces.sort().shift();
                //console.log(shapes, surfaces);
                resolve({ shapes, surfaces });
            })
            .on('error', (error) => {
                reject(error);
            });
        });
}

// Prends la liste des Objets champignons et récupère leurs shapes
function getShapes(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleShapes = new Set(champignons.map(objet => objet.Shape));

    // Convertir l'ensemble en une liste
    return [...ensembleShapes];
}

// Prends la liste des Objets champignons et récupère leurs surfaces
function getSurfaces(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleSurfaces = new Set(champignons.map(objet => objet.Surfaces));

    // Convertir l'ensemble en une liste
    return [...ensembleSurfaces];
}

// Exporter les données récupérées dans le CSV
module.exports = loadCSVData;