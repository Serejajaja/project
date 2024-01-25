from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def markup_button() -> ReplyKeyboardMarkup:
    """ Функция создает кнопки с командами на панели клавиатуры """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)  # Создаем клавиатуру
    # Создаем кнопки всплывающие под клавиатурой
    low = KeyboardButton('Низкий рейтинг 🔽')
    high = KeyboardButton('Высокий рейтинг 🔼')
    custom = KeyboardButton('Выборочный рейтинг 📶')
    history = KeyboardButton('История запросов 📖')
    # Добавляем кнопки
    markup.add(low, high, custom, history)
    return markup  # возвращаем результат
