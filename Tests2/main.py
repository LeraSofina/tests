import requests


class UsersYD:
    def __init__(self, token):
        self.token = token
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        # self.dir_href = None

    def create_folder(self, name_dir: str):
        params = {
            'path': f'/{name_dir}/'
        }
        resp = requests.put(self.url, headers=self.headers, params=params)
        return resp


if __name__ == '__main__':
    user = UsersYD(token='')
    print(user.create_folder('my_new_folder'))

