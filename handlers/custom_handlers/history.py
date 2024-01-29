from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line
from states.user_date import UserState
from config_data.config import type_films_dict, type_meny_check
from database.core import User, History
from typing import List
from time import sleep


# задаем команды на которые бот будет реагировать
@bot.message_handler(func=lambda message: message.text in type_meny_check[3])
def send_history(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    history_list: List[History] = user.history.order_by(-History.number).limit(5)

    if not history_list:
        bot.send_message(message.from_user.id, "У вас еще нет истории")
        return

    mess = 'История последнего запроса'
    bot.send_message(message.from_user.id, mess)  # ответ на сообщение
    for string in history_list:
        format_text = string.film_genres.replace("[", '').replace("]", '').replace("'", '')
        text = (f'Название фильма: {string.film_name}\n'
                f'Год: {string.film_year}\n'
                f'Рейтинг: {string.film_rating}\n'
                f'Постер: {string.film_poster}\n'
                f'Жанр: {format_text}')
        bot.send_message(message.from_user.id, text=text)  # отправляем ответ
        sleep(1)
    bot.set_state(message.from_user.id, UserState.history_user)

