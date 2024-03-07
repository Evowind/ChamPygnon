import requests
import pandas as pd
from bs4 import BeautifulSoup


def comestible(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            tag = soup.find('div', class_='cat_position')
            if tag:
                mushroom_type = tag.find('a').text.strip()
            if "Poisonous" in mushroom_type:
                return "P"
            elif "Edible" in mushroom_type:
                return "E"
            elif "Inedible" in mushroom_type:
                return "I"
            else:
                return ""
        else:
            return ""
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return ""


def color(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            color_tag = soup.find('strong', string='Color:')
            if color_tag:
                mushroom_color = [link.text.strip() for link in color_tag.find_next_siblings('a')]
                # Retourne la valeur mushroom_color sous forme de chaine de caractères
                return '-'.join(str(e) for e in mushroom_color)
            else:
                return []
        else:
            return []
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return []


def shape(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            color_tag = soup.find('strong', string='Shape:')
            if color_tag:
                mushroom_shape = color_tag.find_next('a').text.strip().replace("-", " ")
                return mushroom_shape
            else:
                return ""
        else:
            return ""
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return ""


def surface(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            color_tag = soup.find('strong', string='Surface:')
            if color_tag:
                mushroom_surface = color_tag.find_next('a').text.strip().replace("-", " ")
                return mushroom_surface
            else:
                return ""
        else:
            return ""
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return ""


def csv(url):
    attributes = [comestible(url), color(url), shape(url), surface(url)]
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
        f.write("\n")
        # print(csv(url))

    f.close()
    # print("CSV file name: ", filename)


# Charger le fichier CSV dans un DataFrame
champignons = pd.read_csv("champignons.csv")

import pandas as pd


def preprocess_data(filename):
    # Charger le fichier CSV dans un DataFrame
    champignons = pd.read_csv(filename)

    # Inspecter les données de la colonne "Edible" et visualiser les lignes vides
    print("Valeurs de la colonne 'Edible' :")
    print(champignons['Edible'].value_counts(dropna=False))

    # Remplacer respectivement les valeurs "E", "I" et "P" par 0, 1 et 2
    champignons['Edible'] = champignons['Edible'].replace({'E': 0, 'I': 1, 'P': 2})

    # Vérifier sur quelques lignes de champignons que le résultat est bien celui attendu
    print("\nExemple de quelques lignes après le remplacement :")
    print(champignons.head())

    # Remplacer les valeurs manquantes par -1
    champignons['Edible'].fillna(-1, inplace=True)

    # Comparer le résultat obtenu via value_counts() avec celui obtenu dans la Question 8
    print("\nValeurs de la colonne 'Edible' après le traitement :")
    print(champignons['Edible'].value_counts(dropna=False))

    return champignons


alphabet = "https://ultimate-mushroom.com/mushroom-alphabet.html"
url1 = "https://ultimate-mushroom.com/poisonous/103-abortiporus-biennis.html"
url2 = "https://ultimate-mushroom.com/edible/1010-agaricus-albolutescens.html"
url3 = "https://ultimate-mushroom.com/inedible/452-byssonectria-terrestris.html"

#print("Champignon 1:", comestible(url1), color(url1), shape(url1), surface(url1))
#print("Champignon 2:", comestible(url2), color(url2), shape(url2), surface(url2))
#print("Champignon 3:", comestible(url3), color(url3), shape(url3), surface(url3))
#print("Champignon 4:", csv("https://ultimate-mushroom.com/edible/946-agaricus-langei.html"))
#scrape(alphabet, "champignons.csv")
preprocess_data("champignons.csv")


