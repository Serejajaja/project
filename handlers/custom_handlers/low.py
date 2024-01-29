from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line, markup_line_next
from states.user_date import UserState
from config_data.config import type_films_dict, type_meny_check
from site_API.data_request import string_request
from site_API.core import api_request, headers, check_json, add_history
from database.core import User
from time import sleep


# задаем команды на которые бот будет реагировать
@bot.message_handler(func=lambda message: message.text in type_meny_check[0])
def send_low(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    markup = markup_line()
    mess = 'Выберите категорию с самой низкой оценкой'
    bot.send_message(message.chat.id, mess, reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.low_user, message.chat.id)  # изменение статуса


# сюда получаем сообщение из markup_line
@bot.callback_query_handler(func=lambda call: call.data.isdigit() is True, state=UserState.low_user)
def callback_query(call):
    """
    Функция принимающая возвращаемый ответ после выбора категории пользователем и готовящая запрос по api,
        а так же обработка ответа с api и занесение данных в БД
    """
    print(call.data)  # проверяем поступившие данные
    print(bot.get_state(call.message.from_user.id, call.message.chat.id))  # проверяем состояние

    if call.data in type_films_dict:  # проверяем ответы
        print(type_films_dict[call.data])  # проверяем ответы
        sort_type_data = '1'  # сортировка рейтинга от 0 до 10
        type_number_data = call.data  # тип выбранного фильма
        data_string_request = string_request(sort_type_data=sort_type_data, type_number_data=type_number_data)
        bot.set_state(call.message.from_user.id, UserState.low_user, call.message.chat.id)  # изменение статуса
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
            sleep(2.5)
        add_history(result_json, call.message.chat.id)  # создаем историю запросов пользователя
        with bot.retrieve_data(call.message.chat.id) as data:
            data["type_number_data"] = type_number_data
            data["page_data"] = 2

        # ответ пользователю после списка фильмов
        bot.send_message(call.message.chat.id, text="Следующий список...", reply_markup=markup_line_next())


@bot.callback_query_handler(func=lambda call: call.data == 'next', state=UserState.low_user)
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
            sort_type_data = '1'  # сортировка рейтинга от 0 до 10
            type_number_data = data["type_number_data"]  # тип выбранного фильма
            data_string_request = string_request(page_data=page_data, sort_type_data=sort_type_data, type_number_data=type_number_data)
            bot.set_state(call.message.from_user.id, UserState.low_user, call.message.chat.id)  # изменение статуса
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
