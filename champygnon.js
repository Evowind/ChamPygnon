const csv = require('csv-parser');
const fs = require('fs')

const csvPath = 'champignons.csv';

let champignons = [];
let shapes = [];
let surfaces = [];

// On récupère les informations du CSV
fs.createReadStream(csvPath)
  .pipe(csv())
  .on('data', (data) => champignons.push(data))
  .on('end', () => {
    //console.log(champignons);
    getShapes(champignons);
    getSurfaces(champignons);
    console.log(shapes);
    console.log(surfaces);
});

// On sélectionne les éléments HTML
const shapeContainer = document.getElementById('shapes');
const surfaceContainer = document.getElementById('surfaces');

shapes.forEach(shape => {
    // Créer un nouveau bouton radio qui contient la valeur shape
    let radioBtn = document.createElement('shapeInput');
    radioBtn.type = 'radio';
    radioBtn.name = 'shapeInput';
    radioBtn.value = shape;

    // Créer une étiquette pour le bouton radio
    const label = document.createElement('label');
    label.textContent = option;

    // Ajouter le bouton radio et son étiquette au conteneur
    shapeContainer.appendChild(radioBtn);
    shapeContainer.appendChild(label);
})

surfaceContainer.forEach(surface => {
    // Créer un nouveau bouton radio qui contient la valeur shape
    let radioBtn = document.createElement('surfaceInput');
    radioBtn.type = 'radio';
    radioBtn.name = 'surfaceInput';
    radioBtn.value = surface;

    // Créer une étiquette pour le bouton radio
    const label = document.createElement('label');
    label.textContent = option;

    // Ajouter le bouton radio et son étiquette au conteneur
    surfaceContainer.appendChild(radioBtn);
    surfaceContainer.appendChild(label);
})

function getShapes(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleShapes = new Set(champignons.map(objet => objet.Shape));

    // Convertir l'ensemble en une liste
    shapes = [...ensembleShapes];
    shapes.sort();
}

function getSurfaces(champignons) {
    // Créer un ensemble avec tous les shapes (pour éviter les doublons)
    const ensembleShapes = new Set(champignons.map(objet => objet.Surfaces));

    // Convertir l'ensemble en une liste
    surfaces = [...ensembleShapes];
    surfaces.sort();
}

