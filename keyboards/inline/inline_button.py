from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot


def markup_line() -> InlineKeyboardMarkup:
    """ Функция создания клавиатуры сразу снизу после сообщения """
    markup = InlineKeyboardMarkup()  # Создаем клавиатуру
    # Добавляем кнопки в эту клавиатуру
    markup.add(InlineKeyboardButton('Фильмы',  callback_data='0'),
               InlineKeyboardButton('Сериалы',  callback_data='1'),
               InlineKeyboardButton('Мультфильмы',  callback_data='2'),
               InlineKeyboardButton('Мультсериалы',  callback_data='3'),
               InlineKeyboardButton('Аниме',  callback_data='4'))
    return markup  # возвращаем результат


@bot.callback_query_handler(func=lambda call: True)  # сюда получаем сообщение из markup_line
def callback_query(call):
    """ Функция принимающая возвращаемый ответ после выбора категории пользователем"""
    if call.data == "0":  # проверяем ответы
        bot.answer_callback_query(call.id, "Выбрали Фильмы")
    elif call.data == "1":  # проверяем ответы
        bot.answer_callback_query(call.id, "Выбрали Сериалы")
    elif call.data == "2":  # проверяем ответы
        bot.answer_callback_query(call.id, "Выбрали Мультфильмы")
    elif call.data == "3":  # проверяем ответы
        bot.answer_callback_query(call.id, "Выбрали Мультсериалы")
    elif call.data == "4":  # проверяем ответы
        bot.answer_callback_query(call.id, "Выбрали Аниме")
