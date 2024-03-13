import pandas as pd
import requests
from bs4 import BeautifulSoup


def comestible(url):
    try:
        # Effectuer une requête HTTP pour obtenir le contenu de l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Parser le contenu HTML de la page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Trouver la balise <div> avec la classe 'cat_position'
            tag = soup.find('div', class_='cat_position')
            # Extraire le type de champignon à partir de la balise trouvée
            if tag:
                mushroom_type = tag.find('a').text.strip()
            # Déterminer si le champignon est comestible en fonction du type trouvé
            if "Poisonous" in mushroom_type:
                return "P"  # Champignon vénéneux
            elif "Edible" in mushroom_type:
                return "E"  # Champignon comestible
            elif "Inedible" in mushroom_type:
                return "I"  # Champignon non comestible
            else:
                return ""  # Type de champignon inconnu
        else:
            return ""  # La requête a échoué, pas de type de champignon
    except Exception as e:
        print("Une erreur s'est produite :", e)  # Afficher l'erreur
        return ""  # Retourner une chaîne vide en cas d'erreur


def color(url):
    try:
        # Effectuer une requête HTTP pour obtenir le contenu de l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Parser le contenu HTML de la page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Trouver la balise <strong> contenant le texte 'Color:'
            color_tag = soup.find('strong', string='Color:')
            # Extraire la couleur du champignon à partir de la balise trouvée
            if color_tag:
                mushroom_color = [link.text.strip() for link in color_tag.find_next_siblings('a')]
                # Retourner la valeur mushroom_color sous forme de chaîne de caractères séparée par '-'
                return '-'.join(str(e) for e in mushroom_color)
            else:
                return []  # Aucune couleur trouvée
        else:
            return []  # La requête a échoué, pas de couleur de champignon
    except Exception as e:
        print("Une erreur s'est produite :", e)  # Afficher l'erreur
        return []  # Retourner une liste vide en cas d'erreur


def shape(url):
    try:
        # Effectuer une requête HTTP pour obtenir le contenu de l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Parser le contenu HTML de la page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Trouver la balise <strong> contenant le texte 'Shape:'
            color_tag = soup.find('strong', string='Shape:')
            # Extraire la forme du champignon à partir de la balise trouvée
            if color_tag:
                mushroom_shape = color_tag.find_next('a').text.strip().replace("-", " ")
                return mushroom_shape
            else:
                return ""  # Aucune forme trouvée
        else:
            return ""  # La requête a échoué, pas de forme de champignon
    except Exception as e:
        print("Une erreur s'est produite :", e)  # Afficher l'erreur
        return ""  # Retourner une chaîne vide en cas d'erreur


def surface(url):
    try:
        # Effectuer une requête HTTP pour obtenir le contenu de l'URL
        response = requests.get(url)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Parser le contenu HTML de la page
            soup = BeautifulSoup(response.content, 'html.parser')
            # Trouver la balise <strong> contenant le texte 'Surface:'
            color_tag = soup.find('strong', string='Surface:')
            # Extraire la surface du champignon à partir de la balise trouvée
            if color_tag:
                mushroom_surface = color_tag.find_next('a').text.strip().replace("-", " ")
                return mushroom_surface
            else:
                return ""  # Aucune surface trouvée
        else:
            return ""  # La requête a échoué, pas de surface de champignon
    except Exception as e:
        print("Une erreur s'est produite :", e)  # Afficher l'erreur
        return ""  # Retourner une chaîne vide en cas d'erreur


def csv(url):
    # Appeler les fonctions pour obtenir les attributs du champignon
    attributes = [comestible(url), color(url), shape(url), surface(url)]
    # Retourner les attributs sous forme de chaîne CSV
    return ','.join(str(e) for e in attributes)


def get_list(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            all_href = soup.select('ol li p a[href]')
            href_values = [link['href'] for link in all_href]
            return href_values
        else:
            return []
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return []


def scrape(url, filename):
    url_list = get_list(url)
    if url_list:
        with open(filename, 'w') as f:
            f.write("Edible,Color,Shape,Surface\n")  # Ajout de la première ligne avec les noms de colonnes
            for url in url_list:
                f.write(csv(url))
                f.write("\n")

    # Importer le contenu du CSV dans un DataFrame
    champignons = pd.read_csv(filename)

    # Vérifier les dimensions et les noms de colonnes du DataFrame
    if champignons.shape == (1113, 4) and list(champignons.columns) == ["Edible", "Color", "Shape", "Surface"]:
        print("Le jeu de données possède 1113 lignes et 4 attributs avec les bons noms.")
    else:
        print("Erreur: Le jeu de données ne possède pas les dimensions ou les noms de colonnes attendus.")


def write_to_csv(url_list, filename):
    f = open(filename, 'w')
    # Pour chaque lien de champignon, obtenir les caractéristiques et écrire dans le fichier CSV
    for url in url_list:
        f.write(csv(url))
        f.write("\n")  # print(csv(url))
    f.close()  # print("CSV file name: ", filename)


def preprocess_data(filename):
    # Charger le fichier CSV dans un DataFrame
    champignons = pd.read_csv(filename)

    # Inspecter les données de la colonne "Edible" et visualiser les lignes vides
    print("Valeurs de la colonne 'Edible' :")
    print(champignons['Edible'].value_counts(dropna=False))

    # Remplacer respectivement les valeurs "E", "I" et "P" par 0, 1 et 2
    # TODO : Enlever le no_silent_downcasting et resoudre le problème de FuturWarning
    pd.set_option('future.no_silent_downcasting', True)
    champignons['Edible'] = champignons['Edible'].replace({'E': 0, 'I': 1, 'P': 2})

    # Vérifier sur quelques lignes de champignons que le résultat est bien celui attendu
    print("\nExemple de quelques lignes après le remplacement :")
    print(champignons.head())

    # Remplacer les valeurs manquantes par -1
    champignons['Edible'] = champignons['Edible'].fillna(-1)

    # Comparer le résultat obtenu via value_counts() avec celui obtenu dans la Question 8
    print("\nValeurs de la colonne 'Edible' après le traitement :")
    print(champignons['Edible'].value_counts(dropna=False))

    return champignons


def create_indicator_columns(df, column_names):
    print(f"\nNouveau DataFrame avec colonnes indicateurs : {column_names} remplacées.")
    for column_name in column_names:
        # Récupérer la liste de toutes les valeurs uniques dans la colonne
        unique_values = pd.unique(df[column_name].str.split("-").explode().dropna())

        # Remplacer les valeurs NaN par une chaîne vide
        df[column_name] = df[column_name].fillna("")

        # Ajouter une nouvelle colonne pour chaque valeur unique
        for value in unique_values:
            # Skip if value is 'shaped' as part of the column name
            if value.lower() == 'shaped':
                continue
            df[f"{column_name}_{value}"] = df[column_name].str.contains(value).astype(int)

    # Supprimer les colonnes spécifiées
    df = df.drop(column_names, axis=1)

    # Afficher toutes les colonnes du DataFrame
    pd.set_option('display.max_columns', None)
    # Afficher les premières lignes du DataFrame pour vérifier le résultat
    print(df.head())
    print(df.shape)
    return df


def get_unique_colors(df):
    unique_colors = df['Color'].str.split("-").explode().dropna().unique()
    for index, row in df.iterrows():
        colors = row['Color']
        if isinstance(colors, list):  # Check if colors is a list (not NaN)
            unique_colors.update(colors)
    return unique_colors


import pandas as pd

def create_color_dataframe():
    # Dictionnaire des couleurs en RGB
    color_dict = {
        'Pale': (255, 255, 211),
        'White': (255, 255, 255),
        'Yellow': (255, 255, 0),
        'Brown': (165, 42, 42),
        'Pink': (255, 192, 203),
        'Purple': (128, 0, 128),
        'Tan': (210, 180, 140),
        'Orange': (255, 165, 0),
        'Gray': (128, 128, 128),
        'Red': (255, 0, 0),
        'Dark': (0, 0, 139),
        'Green': (0, 128, 0),
        'Blue': (0, 0, 255),
        'Violet': (238, 130, 238),
        'Lilac': (200, 162, 200)
    }
    # Créer un DataFrame à partir du dictionnaire
    df = pd.DataFrame(list(color_dict.items()), columns=['Color', 'RGB'])
    # Diviser la colonne 'RGB' en trois colonnes distinctes pour R, G, et B
    df[['R', 'G', 'B']] = pd.DataFrame(df['RGB'].tolist(), index=df.index)
    # Supprimer la colonne 'RGB' qui n'est plus nécessaire
    df = df.drop('RGB', axis=1)
    return df


alphabet = "https://ultimate-mushroom.com/mushroom-alphabet.html"
url1 = "https://ultimate-mushroom.com/poisonous/103-abortiporus-biennis.html"
url2 = "https://ultimate-mushroom.com/edible/1010-agaricus-albolutescens.html"
url3 = "https://ultimate-mushroom.com/inedible/452-byssonectria-terrestris.html"

# print("Champignon 1:", comestible(url1), color(url1), shape(url1), surface(url1))
# print("Champignon 2:", comestible(url2), color(url2), shape(url2), surface(url2))
# print("Champignon 3:", comestible(url3), color(url3), shape(url3), surface(url3))
# print("Champignon 4:", csv("https://ultimate-mushroom.com/edible/946-agaricus-langei.html"))
# scrape(alphabet, "champignons.csv")
preprocess_data("champignons.csv")

# 2.3 Colonnes “Shape” et “Surface”
# Appel de la fonction pour ajouter des colonnes indicatrices pour remplacer la colonne "Shape" et la colonne "Surface"
champignons = create_indicator_columns(pd.read_csv("champignons.csv"), ['Shape', 'Surface'])

# 2.4 Colonne “Color”
unique = get_unique_colors(champignons)
print("Liste des couleurs individuelles présentes dans le jeu de données:", unique)
print("Nombre de couleurs individuelles:", len(unique))

# Appeler la fonction pour obtenir le DataFrame
color_df = create_color_dataframe()
print(color_df)
