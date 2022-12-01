import requests
import os


class YaUploader:
    base_url = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, path):
        uri = 'v1/disk/resources/upload'
        request_url = self.base_url + uri
        params = {'path': path, 'overwrite': True}
        response = requests.get(request_url, headers=self._get_headers(), params=params)

        return response.json()['href']

    def upload(self, file_path: str):
        # Будем класть файлы в корень диска (по заданию не обозначен желаемый путь), но можно и добавить
        # дополнительным параметром.
        name = os.path.basename(file_path)
        path = f'/{name}'
        upload_url = self._get_upload_link(path)
        response = requests.put(upload_url, data=open(file_path, 'rb'), headers=self._get_headers())

        if response.status_code == 201:
            print('Готово!')
