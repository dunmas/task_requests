import requests


class Superheroes:

    base_url = 'https://akabab.github.io/superhero-api/api'
    heroes = dict()

    def __init__(self, *necessary_heroes):
        all_heroes = self._get_superheroes_dict()

        for hero in necessary_heroes:
            self.heroes[hero] = all_heroes[hero]

    def _get_superheroes_dict(self):
        uri = '/all.json'
        request_url = self.base_url + uri
        response = requests.get(request_url)
        heroes_base = dict()

        for hero in response.json():
            heroes_base[hero['name']] = hero

        return heroes_base

    def sort_by_intelligence(self):
        buffer = dict()

        for hero in self.heroes:
            buffer[self.heroes[hero]['powerstats']['intelligence']] = self.heroes[hero]['name']

        buffer = sorted(buffer.items(), reverse=True)

        for count, hero in enumerate(buffer):
            print(f"#{count + 1} - {hero[1]} ({hero[0]} intelligence points)")



