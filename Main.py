import requests
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
                return mushroom_color
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
                mushroom_shape = color_tag.find_next('a').text.strip()
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
                mushroom_surface = color_tag.find_next('a').text.strip()
                return mushroom_surface
            else:
                return ""
        else:
            return ""
    except Exception as e:
        print("Une erreur s'est produite :", e)
        return ""


def tostring(colors):
    return '-'.join(str(e) for e in colors)


url1 = "https://ultimate-mushroom.com/poisonous/103-abortiporus-biennis.html"
url2 = "https://ultimate-mushroom.com/edible/1010-agaricus-albolutescens.html"
url3 = "https://ultimate-mushroom.com/inedible/452-byssonectria-terrestris.html"

print("Champignon 1:", comestible(url1), color(url1), shape(url1), surface(url1))
print("Champignon 2:", comestible(url2), tostring(color(url2)), shape(url2), surface(url2))
print("Champignon 3:", comestible(url3), color(url3), shape(url3), surface(url3))

