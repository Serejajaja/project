from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def markup_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    low = KeyboardButton('/low')
    high = KeyboardButton('/high')
    custom = KeyboardButton('/custom')
    history = KeyboardButton('/history')
    markup.add(low, high, custom, history)
    return markup
