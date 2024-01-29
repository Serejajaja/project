from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def markup_line() -> InlineKeyboardMarkup:
    """ Функция создания клавиатуры сразу снизу после сообщения """
    markup = InlineKeyboardMarkup()  # Создаем клавиатуру
    # Добавляем кнопки в эту клавиатуру
    markup.add(InlineKeyboardButton('Фильмы 🎬',  callback_data='1'),
               InlineKeyboardButton('Сериалы 🍿',  callback_data='2'),
               InlineKeyboardButton('Мультфильмы 🎠',  callback_data='3'),
               InlineKeyboardButton('Аниме 🎎',  callback_data='4'),
               InlineKeyboardButton('Мультсериалы 🏰',  callback_data='5'))
    return markup  # возвращаем результат


def markup_line_next() -> InlineKeyboardMarkup:
    """ Функция создания клавиатуры сразу снизу после сообщения """
    markup = InlineKeyboardMarkup()  # Создаем клавиатуру
    # Добавляем кнопки в эту клавиатуру
    markup.add(InlineKeyboardButton('Дальше 🔜',  callback_data='next'))
    return markup  # возвращаем результат
