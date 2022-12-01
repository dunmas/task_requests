from time import time
import requests

# Двухдневный промежуток
TIME_GAP = 172800


def get_tagged_questions_json(tag: str):
    questions_link = 'https://api.stackexchange.com/2.3/questions'
    today = int(time())
    params = {
        'site': 'stackoverflow',
        'sort': 'activity',
        'order': 'desc',
        'tagged': tag,
        'fromdate': today - TIME_GAP,
        'todate': today,
    }

    return requests.get(questions_link, params=params).json()
