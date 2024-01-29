from time import sleep
from typing import List
from config_data.config import type_meny_check
from database.core import History, User
from loader import bot
from states.user_date import UserState
from telebot.types import Message


# задаем команды на которые бот будет реагировать
@bot.message_handler(func=lambda message: message.text in type_meny_check[3])
def send_history(message: Message) -> None:
    """
    Проверяем наличие пользователя в БД и обрабатываем введенную команду.
    Выдаем пользователю историю его запросов
    """
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)  # Сравниваем id юзера с БД

    if user is None:  # Проверяем регистрацию пользователя
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    history_sked: List[History] = user.history.order_by(-History.number).limit(5)  # создаем список истории из БД

    if not history_sked:  # Проверяем наличие истории
        bot.send_message(message.from_user.id, "У вас еще нет истории")
        return

    mess = 'История последнего запроса'
    bot.send_message(message.from_user.id, mess)  # ответ на сообщение

    for string in history_sked:
        format_text = string.film_genres.replace("[", '').replace("]", '').replace("'", '')  # фильтруем строку
        text = (f'Название фильма: {string.film_name}\n'
                f'Год: {string.film_year}\n'
                f'Рейтинг: {string.film_rating}\n'
                f'Постер: {string.film_poster}\n'
                f'Жанр: {format_text}')
        bot.send_message(message.from_user.id, text=text)  # отправляем ответ
        sleep(1)  # плавно выдаем ответы
    bot.set_state(message.from_user.id, UserState.history_user)
