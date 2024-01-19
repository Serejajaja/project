import requests

from config_data.config import SiteSettings

config = SiteSettings()

headers = {'X-API-KEY': config.API_KEY.get_secret_value()}


def api_request(headers: dict) -> requests.Response:
    return requests.get(config.API_URL, headers=headers)


result = api_request(headers)
print(result.text)


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