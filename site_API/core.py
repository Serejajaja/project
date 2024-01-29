import json
import os
from typing import Any
from config_data.config import SiteSettings
from database.core import History
import requests


config = SiteSettings()  # загружаем настройки

headers = {'X-API-KEY': config.API_KEY.get_secret_value()}  # заголовок для подключения к api


def api_request(string_data: str, headers: dict) -> requests.Response:
    """ Отправляем запрос на api и возвращаем результат """
    my_req = requests.get(config.API_URL + string_data, headers=headers)  # Отправили составной api запрос
    result = json.loads(my_req.text.replace('\xa0', ' '))  # Сделали из текста словарь и удалили лишний символ
    with open('result.json', 'w', encoding='utf8') as file:  # Загрузили в json Файл для удобства просмотра
        json.dump(result, file, ensure_ascii=False, indent=4)
    with open(os.path.abspath(os.path.join('result.json')), 'r', encoding='utf8') as file:
        data_file = json.load(file)
    return data_file


def check_json(file_new: Any) -> list:
    """ Данная функция обрабатывает json файл и возвращает список со словарями по каждому фильму"""
    key_list = ["id", "name", "year"]
    total_list = list()
    step_range = 0
    range_list = len(file_new['docs'])  # получаем длину списка фильмов
    while step_range != range_list:  # значение равно количеству выгружаемых результатов
        data = file_new['docs'][step_range]
        step_dict = dict()
        for key in data:  # проходимся циклом по ключам словаря
            if key in key_list:
                if data[key] is None:
                    if key == "name":
                        step_dict["name"] = data["alternativeName"]
                    else:
                        step_dict[key] = 'Нет'
                else:
                    step_dict[key] = data[key]
            if key == "rating":
                if data[key] is None:
                    step_dict[key] = 'Нет'
                else:
                    step_dict[key] = data[key]["kp"]
            if key == "poster":
                if data[key]["url"] is None:
                    step_dict[key] = 'Нет'
                else:
                    step_dict[key] = data[key]["url"]
            if key == "genres":
                genres_list = list()
                for index in data[key]:
                    genres_list.append(index["name"])
                step_dict[key] = genres_list
        step_range += 1
        total_list.append(step_dict)  # добавляем результат по одному фильму в общий список
    return total_list


def add_history(data: Any, user_id: int) -> None:
    """ Добавляем фильм БД и связываем его с пользователем"""
    for position in data:
        History.create(
            user=user_id,
            film_id=position["id"],
            film_name=position["name"],
            film_year=position["year"],
            film_rating=position["rating"],
            film_poster=position["poster"],
            film_genres=position["genres"],
        )
