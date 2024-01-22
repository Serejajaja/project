import requests
import json

from config_data.config import SiteSettings
from site_API.data_request import string_request
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
