const express = require('express')
const fs = require('fs').promises;
const { exec } = require('child_process');

const app = express()
app.use(express.json());
app.set('view engine', 'ejs');
const {shapes, surfaces} = require('./champygnon');

// Redirect
app.get('/', (req, res) => {
    res.redirect('/form');
});

// Route GET à l'URL "/form"
app.get('/form', async (req, res) => {
    try {
        //const contenuFormulaire = await fs.readFile('views/formulaire.html', 'utf8');
        //res.send(contenuFormulaire);
        console.log("When route GET");
        console.log(shapes);
        console.log(surfaces);
        res.render('formulaire', {shapes, surfaces});
    } catch (err) {
        console.error("Erreur lors de la lecture du fichier: ", err);
        res.status(500).send("Une erreur est survenue lors de la lecture du fichier.");
    }
});

// Route POST à l'URL "/rep"
app.post('/rep', async (req, res) => {
    try {
        // Lecture des données envoyées dans le formulaire
        const redValue = req.body['red-value'];
        const blueValue = req.body['blue-value'];
        const greenValue = req.body['green-value'];
        const model = req.body.selectmodel;
        const shape = req.body.radioShape;
        const surface = req.body.radioSurface;

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
// Peut-être mettre les deux sur le meme url avec app.route('/form').get({}).post({})

// Démarrer le serveur
app.listen(3000, () => {
    console.log( " Listening ... ");
});