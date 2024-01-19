from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def markup_line():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Фильм',  callback_data='0'),
                   InlineKeyboardButton('Сериал',  callback_data='1'),
                   InlineKeyboardButton('Мультик',  callback_data='2'),
                   InlineKeyboardButton('Аниме',  callback_data='3'))
    return markup  # возвращаем результат
