import sys
import pickle

def predict(model_path, features):
    # Charger le modèle entraîné
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    # Préparer les caractéristiques pour la prédiction
    redValue, blueValue, greenValue, shape, surface = features[:5]
    # Convertir les caractéristiques catégorielles au format encodé one-hot
    shape_encoded = [1 if s == shape else 0 for s in ['Polypore', 'Convex', 'Bell', 'Depressed', 'CupFungi', 'CoralFungi', 'Conical', 'Flat', 'JellyFungi', 'Stinkhorns', 'Earthstars', 'Puffballs', 'Corticioid', 'Chanterelles', 'Funnel', 'Cylindrical', 'Knobbed', 'Shell', 'Truffles', 'Bolete', 'FalseMorels', 'ToothFungi', 'TrueMorels', 'Cauliflower']]
    surface_encoded = [1 if s == surface else 0 for s in ['Smooth', 'FlatScales', 'Fibrous', 'Patches', 'RaisedScales', 'Hairy', 'Powder', 'Silky', 'Velvety']]

    # Combinaison de toutes les caractéristiques
    feature_values = [float(redValue), float(blueValue), float(greenValue)] + shape_encoded + surface_encoded

    # Faire des prédictions
    predictions = model.predict([feature_values])

    return predictions[0]

if __name__ == "__main__":
    # Obtenir le chemin du modèle et les caractéristiques à partir des arguments de la ligne de commande
    model_path = sys.argv[1]
    features = sys.argv[2:]

    # Effectuer la prédiction
    result = predict(model_path, features)

    # Afficher le résultat
    print(result)
