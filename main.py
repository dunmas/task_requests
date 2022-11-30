import requests
import json


class Superheroes:

    base_url = 'https://akabab.github.io/superhero-api/api'
    heroes = dict()

    def __init__(self, *heroes):
        all_heroes = self._get_superheroes_dict()

        for hero in heroes:
            self.heroes[hero] = all_heroes[hero]

    def _get_superheroes_dict(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        heroes_base = dict()

        for hero in response.json():
            heroes_base[hero['name']] = hero

        return heroes_base

    def get_list(self):
        print(self.heroes)


money = Superheroes('Hulk', 'Superman')
