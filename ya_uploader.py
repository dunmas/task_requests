from token import TOKEN


class YaUploader:
    base_url = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path: str):
        pass


if __name__ == '__main__':
    path_to_file = ''
    token = TOKEN
    uploader = YaUploader(token)

    uploader.upload(path_to_file)
