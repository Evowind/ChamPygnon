import sys
import pickle
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Récupérer les arguments passés en ligne de commande
model_name = sys.argv[1]
red = int(sys.argv[2])
blue = int(sys.argv[3])
green = int(sys.argv[4])
shape = sys.argv[5]
surface = sys.argv[6]

# Charger le modèle sauvegardé
if model_name == 'svm':
    with open('svm_model.pkl', 'rb') as f:
        model = pickle.load(f)
elif model_name == 'tree':
    with open('tree_model.pkl', 'rb') as f:
        model = pickle.load(f)
else:
    print("Modèle inconnu")
    sys.exit(1)

# Préparer les données d'entrée
X_new = [[red, blue, green, shape, surface]]

# Faire la prédiction
y_pred = model.predict(X_new)

# Renvoyer la prédiction
print(y_pred[0])
