from pprint import pprint

import requests

# from reddit import Reddit
# from ya_disk import YandexDisk

# TOKEN = ""


def hero_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    intelligence = 0
    hero_name = ''
    for record in response.json():
        if record['name'] == 'Thanos':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']
        if record['name'] == 'Hulk':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']
        if record['name'] == 'Captain America':
            for key, value in record.items():
                if key == 'powerstats':
                    for powerstats in value:
                        if value['intelligence'] > intelligence:
                            intelligence = value['intelligence']
                            hero_name = record['name']

    print(f'Самый умный герой: {hero_name}')
    print(f'Уровень интеллекта: {intelligence}')
    # print(record)


if __name__ == '__main__':
    hero_request()
