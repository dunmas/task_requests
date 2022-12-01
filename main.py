from superheroes import Superheroes
from ya_uploader import YaUploader
from stack_questions import get_tagged_questions_json
import json
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

    # Задание 3
    question_tag = 'Python'
    questions_json = get_tagged_questions_json(question_tag)
    # Проверяем вывод (закомментил для удобства просмотра предыдущих заданий)
    #print(json.dumps(questions_json, indent=2))
