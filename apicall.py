import requests
from random import randint


def random_xkcd():
    comic_number = randint(0, 3057)

    response = requests.get(f"https://xkcd.com/{comic_number}/info.0.json")
    data = response.json()
    return data