import sys
import joblib

def load_models(model_name):
    # Charger le modèle depuis le fichier pickle
    model_path = f"/{model_name}.pkl"
    model = joblib.load(model_path)
    return model

def predict(model, red_value, green_value, blue_value, shape, surface):
    # Exemple de prétraitement des caractéristiques
    features = [red_value, green_value, blue_value, shape, surface]

    # Effectuer la prédiction avec le modèle spécifié
    prediction = model.predict([features])  # Assurez-vous que les caractéristiques sont dans le bon format pour votre modèle

    return prediction

if __name__ == "__main__":
    # Récupérer les arguments passés depuis le script Node.js
    model_name = sys.argv[1]
    red_value = float(sys.argv[2])
    green_value = float(sys.argv[3])
    blue_value = float(sys.argv[4])
    shape = sys.argv[5]
    surface = sys.argv[6]

    # Charger le modèle spécifié
    model = load_models(model_name)

    # Effectuer la prédiction
    result = predict(model, red_value, green_value, blue_value, shape, surface)

    # Afficher le résultat de la prédiction
    print(result)
