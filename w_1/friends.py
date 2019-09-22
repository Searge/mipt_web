import requests
import datetime

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'


def get_user_id(uid):
    request = 'https://api.vk.com/method/users.get?v=5.71&access_token={}&user_ids={}'.format(
        ACCESS_TOKEN,
        uid)
    response = requests.get(request)
    if response.status_code == requests.codes.ok:
        return response.json()['response'][0]['id']


def get_user_friends(uid):
    request = 'https://api.vk.com/method/friends.get?v=5.71&access_token={}&user_id={}&fields=bdate'.format(
        ACCESS_TOKEN, uid)
    response = requests.get(request)
    if response.status_code == requests.codes.ok and 'error' not in response:
        return response.json()['response']['items']


def calc_age(uid):
    year_of_birth = [yob['bdate'].split('.')[2]
                     for yob in get_user_friends(uid)
                     if yob.get('bdate', None) != None and len(yob['bdate'].split('.')) == 3]
    return sorted(
        [(datetime.datetime.now().year - int(x),
          year_of_birth.count(x)) for x in set(year_of_birth)],
        key=lambda point: (point[1],
                           -point[0]),
        reverse=True)


if __name__ == '__main__':
    user_id = get_user_id('reigning')
    res = calc_age(user_id)
    print(res)
