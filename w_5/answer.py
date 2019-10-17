import json
import requests
from base64 import b64encode


def headers(login: str = 'alladin', password: str = 'opensesame'):
    pwdd = {'login': login, 'password': password}
    pwd = ':'.join(pwdd.values()).encode()
    encr = b64encode(pwd).decode()

    return {'Authorization': f'Basic {encr}'}


def url(path: str = 'submissions/1/'):
    return f'http://79.137.175.13/{path}'


if __name__ == '__main__':
    post = requests.post(url(), headers=headers()).json()
    put = requests.put(
        url(post['path']),
        headers=headers(login=post['login'], password=post['password'])
    ).json()
    with open('answer.txt', 'w') as f:
        f.write(put['answer'])
