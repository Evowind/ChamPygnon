const express = require('express')
const bodyParser = require('body-parser');
const fs = require('fs').promises;
const { exec } = require('child_process');

const app = express()
app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.set('view engine', 'ejs');
const loadCSVData  = require('./champygnon');

// Redirect
app.get('/', (req, res) => {
    res.redirect('/form');
});

// Route GET à l'URL "/form"
app.get('/form', async (req, res) => {
    try {
        const { shapes, surfaces } = await loadCSVData();
        console.log("route get: ");
        console.log(shapes, surfaces);
        res.render('formulaire', {shapes, surfaces});
    } catch (error) {
        console.error('Error loading CSV data:', error);
        res.status(500).send('Error loading CSV data');
  }
});

// Route POST à l'URL "/rep"
app.post('/rep', async (req, res) => {
    try {
        // Lecture des données envoyées dans le formulaire
        const redValue = req.body['red-value'];
        const blueValue = req.body['blue-value'];
        const greenValue = req.body['green-value'];
        const shape = req.body.shape;
        const surface = req.body.surface;
        const model = req.body.selectmodel;

        // Exécuter le script Python avec les données du formulaire
        exec(`python prediction.py ${model} ${redValue} ${blueValue} ${greenValue} ${shape} ${surface}`, (error, stdout, stderr) => {
            if (error) {
                console.error("Erreur lors de l'exécution du script Python :", error);
                res.status(500).send("Une erreur est survenue lors de l'exécution du script Python.");
                return;
            }
            // Renvoyer la sortie du script Python comme réponse
            res.send(stdout);
        });
    } catch (err) {
        console.error('Erreur lors du traitement de la requête POST :', err);
        res.status(500).send('Une erreur est survenue lors du traitement de la requête POST.');
    }
});

// Démarrer le serveur
app.listen(3000, () => {
    console.log( " Listening ... ");
});