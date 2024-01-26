from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line, markup_line_next
from states.user_date import UserState
from config_data.config import type_films_dict, type_meny_check
from site_API.data_request import string_request
from site_API.core import api_request, headers, check_json, add_history
from database.core import User


# задаем команды на которые бот будет реагировать
@bot.message_handler(func=lambda message: message.text in type_meny_check[2])
def send_custom(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    mess = ('Задайте свои данные для поиска!\n'
            'Введите С какого года искать YYYY:')
    bot.send_message(message.chat.id, mess)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.question_1, message.chat.id)  # изменение статуса


@bot.message_handler(state=UserState.question_1)
def request_year_down(message: Message) -> None:
    if not message.text.isdigit():
        bot.send_message(message.from_user.id, "Год не может быть текстом:")
        return
    if int(message.text) < 1874:
        bot.send_message(message.from_user.id, "Год не может быть меньше 1874:")
        return
    if int(message.text) > 2050:
        bot.send_message(message.from_user.id, "Год не может быть больше 2050:")
        return
    bot.send_message(message.from_user.id, "Введите ПО какой год искать YYYY:")
    bot.set_state(message.from_user.id, UserState.question_2, message.chat.id)
    with bot.retrieve_data(message.from_user.id) as data:
        data["year_down"] = message.text


@bot.message_handler(state=UserState.question_2)
def request_year_up(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        if not message.text.isdigit():
            bot.send_message(message.from_user.id, "Год не может быть текстом:")
            return
        if int(message.text) < int(data["year_down"]):
            text = f"Год не может быть меньше {data['year_down']}"
            bot.send_message(message.from_user.id, text=text)
            return
        if int(message.text) > 2050:
            bot.send_message(message.from_user.id, "Год не может быть больше 2050:")
            return
        bot.send_message(message.from_user.id, "Введите минимальный рейтинг 0 - 10:")
        bot.set_state(message.from_user.id, UserState.question_3, message.chat.id)
        data["year_up"] = message.text


@bot.message_handler(state=UserState.question_3)
def request_rating_down(message: Message) -> None:
    if not message.text.isdigit():
        bot.send_message(message.from_user.id, "Рейтинг не может быть текстом:")
        return
    if int(message.text) < 0 or int(message.text) > 10:
        text = f"Рейтинг должен быть в диапазоне 0 - 10"
        bot.send_message(message.from_user.id, text=text)
        return
    bot.send_message(message.from_user.id, "Введите максимальный рейтинг 0 - 10:")
    bot.set_state(message.from_user.id, UserState.question_4, message.chat.id)
    with bot.retrieve_data(message.from_user.id) as data:
        data["rating_down"] = message.text


@bot.message_handler(state=UserState.question_4)
def request_rating_up(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id) as data:
        if not message.text.isdigit():
            bot.send_message(message.from_user.id, "Год не может быть текстом:")
            return
        if int(message.text) < 0 or int(message.text) > 10:
            text = f"Рейтинг должен быть в диапазоне 0 - 10"
            bot.send_message(message.from_user.id, text=text)
            return
        if int(message.text) < int(data["rating_down"]):
            text = f"Рейтинг не может быть меньше {data['rating_down']}"
            bot.send_message(message.from_user.id, text=text)
            return
    bot.send_message(message.from_user.id, "Выберите категорию:", reply_markup=markup_line())
    bot.set_state(message.from_user.id, UserState.custom_user, message.chat.id)
    data["rating_up"] = message.text

    print(data["year_down"])
    print(data["year_up"])
    print(data["rating_down"])
    print(data["rating_up"])

# ОСТАНОВИЛСЯ НА ТОМ  ЧТО НУЖНО СДЕЛАТЬ СТРОКУ ДЛЯ ЗАПРОСА
# НАДО ПЕРЕДЕЛАТЬ list_next


# # сюда получаем сообщение из markup_line
@bot.callback_query_handler(func=lambda call: call.data.isdigit() is True, state=UserState.custom_user)
def callback_query(call):
    """
    Функция принимающая возвращаемый ответ после выбора категории пользователем и готовящая запрос по api,
        а так же обработка ответа с api и занесение данных в БД
    """

    with bot.retrieve_data(call.message.chat.id) as data:
        print(call.data)  # проверяем поступившие данные
        print(bot.get_state(call.message.from_user.id, call.message.chat.id))  # проверяем состояние

        if call.data in type_films_dict:  # проверяем ответы
            print(type_films_dict[call.data])  # проверяем ответы
            if data["year_down"] == data["year_up"]:
                year_data = data["year_down"]
            else:
                year_data = f'{data["year_down"]}-{data["year_up"]}'
            if data["rating_down"] == data["rating_up"]:
                rating_data = data["rating_down"]
            else:
                rating_data = f'{data["rating_down"]}-{data["rating_up"]}'
            sort_type_data = '-1'  # сортировка рейтинга от 10 до 0
            type_number_data = call.data  # тип выбранного фильма
            data_string_request = string_request(sort_type_data=sort_type_data, type_number_data=type_number_data,
                                                 year_data=year_data, rating_data=rating_data)
            bot.set_state(call.message.from_user.id, UserState.custom_user, call.message.chat.id)  # изменение статуса
            print(bot.get_state(call.message.from_user.id, call.message.chat.id))  # проверяем состояние
            print(data_string_request)  # проверяем строку
            api_result = api_request(data_string_request, headers)  # делаем запрос на api и получаем файл с ответом
            result_json = check_json(api_result)  # обрабатываем файл и получаем выборку

            if len(result_json) == 0:
                bot.send_message(call.message.chat.id, text="Результатов нет. Составьте новый запрос.")
                return

            for index in result_json:  # формируем ответ пользователю по результатам запроса
                format_text = ', '.join(index["genres"])
                text = (f'Название фильма: {index["name"]}\n'
                        f'Год: {index["year"]}\n'
                        f'Рейтинг: {index["rating"]}\n'
                        f'Постер: {index["poster"]}\n'
                        f'Жанр: {format_text}')
                bot.send_message(call.message.chat.id, text=text)  # отправляем ответ
            add_history(result_json, call.message.chat.id)  # создаем историю запросов пользователя
            data["type_number_data"] = type_number_data
            data["page_data"] = 2
            data["year_data"] = year_data
            data["rating_data"] = rating_data

            # ответ пользователю после списка фильмов
            bot.send_message(call.message.chat.id, text="Следующий список...", reply_markup=markup_line_next())


@bot.callback_query_handler(func=lambda call: call.data == 'next', state=UserState.custom_user)
def callback_query_next(call):

    """
    Функция принимающая возвращаемый ответ от пользователя на запрос следующих фильмов и готовящая запрос по api,
        а так же обработка ответа с api и занесение данных в БД
    """

    with bot.retrieve_data(call.message.chat.id) as data:
        print(call.data)  # проверяем поступившие данные
        print(bot.get_state(call.message.from_user.id, call.message.chat.id))  # проверяем состояние

        if call.data == 'next':  # проверяем ответы
            page_data = str(data["page_data"])  # номер страницы для выгрузки
            year_data = data["year_data"]
            rating_data = data["rating_data"]
            sort_type_data = '-1'  # сортировка рейтинга от 10 до 0
            type_number_data = data["type_number_data"]  # тип выбранного фильма
            data_string_request = string_request(page_data=page_data, sort_type_data=sort_type_data,
                                                 type_number_data=type_number_data, year_data=year_data,
                                                 rating_data=rating_data)
            bot.set_state(call.message.from_user.id, UserState.custom_user, call.message.chat.id)  # изменение статуса
            print(bot.get_state(call.message.from_user.id, call.message.chat.id))  # проверяем состояние
            print(data_string_request)  # проверяем строку
            api_result = api_request(data_string_request, headers)  # делаем запрос на api и получаем файл с ответом
            result_json = check_json(api_result)  # обрабатываем файл и получаем выборку

            for index in result_json:  # формируем ответ пользователю по результатам запроса
                format_text = ', '.join(index["genres"])
                text = (f'Название фильма: {index["name"]}\n'
                        f'Год: {index["year"]}\n'
                        f'Рейтинг: {index["rating"]}\n'
                        f'Постер: {index["poster"]}\n'
                        f'Жанр: {format_text}')
                bot.send_message(call.message.chat.id, text=text)  # отправляем ответ
            add_history(result_json, call.message.chat.id)  # создаем историю запросов пользователя

            # ответ пользователю после списка фильмов
            bot.send_message(call.message.chat.id, text="Следующий список...", reply_markup=markup_line_next())
            data["page_data"] += 1  # увеличиваем счетчик страниц
