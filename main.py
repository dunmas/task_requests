from superheroes import Superheroes
from ya_uploader import YaUploader
from settings import TOKEN

if __name__ == '__main__':
    # Задание 1
    set_of_heroes = Superheroes('Hulk', 'Captain America', 'Thanos')
    set_of_heroes.sort_by_intelligence()

    # Задание 2
    path_to_file = 'C:\\Users\\levaf\\Downloads\\6863625.jpg'
    token = TOKEN
    uploader = YaUploader(token)

    uploader.upload(path_to_file)
