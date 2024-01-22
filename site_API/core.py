import requests

from config_data.config import SiteSettings
from data_request import string_request
import json
from pprint import pprint

config = SiteSettings()  # загружаем настройки

headers = {'X-API-KEY': config.API_KEY.get_secret_value()}  # заголовок для подключения к api

string_data = string_request()  # Собираем строку запроса


def api_request(headers: dict) -> requests.Response:
    """ Отправляем запрос на api и возвращаем результат """
    return requests.get(config.API_URL + string_data, headers=headers)


my_req = api_request(headers)  # Результат запроса в виде текста
result = json.loads(my_req.text.replace('\xa0', ' '))  # Сделали из текста словарь и удалили лишний символ
with open('result.json', 'w', encoding='utf8') as file:  # Загрузили в json Файл для удобства просмотра
    json.dump(result, file, ensure_ascii=False, indent=4)
pprint(result)  # Вывода результата запроса


# def api_request(endpoint: str) -> requests.Response:
#     params['key'] = API_KEY
#     return requests.get(
#         f'{site.API_URL}/{endpoint}',
#         params=params
#     )
#
#
# def get_langs() -> List[str]:
#     response = api_request('getLangs');
#     return response.json()
#
#
# def lookup(lang: str, text: str, ui: str = 'ru') -> Dict:
#     response = api_request('lookup', params={
#         'lang': lang,
#         'text': text,
#         'ui': ui
#     })
#
#     return response.json().get('def', {})
#
# langs_response = get_langs()
# if langs_response.status_code != 200:
#     print('Не удалось получить список направлений перевода')
#     exit(1)
#
# langs = langs_response.json()
# print('Выберите одно из доступных направлений перевода')
# print(langs)
# while (lang := input('Введите направление: ')) not in langs:
#     print('Такого направления нет. Попробуйте ещё раз')
#
# text = input('Введите слово или фразу для перевода: ')
# lookup_response = lookup(lang, text)
# if lookup_response.status_code != 200:
#     print('Не удалось выполнить перевод:', lookup_response.text)
#     exit(1)
#
# pprint(lookup_response.json())