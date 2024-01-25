from telebot.types import Message

from loader import bot
from keyboards.inline.inline_button import markup_line
from states.user_date import UserState
from config_data.config import type_films_dict, type_meny_check
from database.core import User


# задаем команды на которые бот будет реагировать
@bot.message_handler(func=lambda message: message.text in type_meny_check[2])
def send_custom(message: Message) -> None:
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    markup = markup_line()
    mess = 'Задайте свои данные для поиска'
    bot.send_message(message.chat.id, mess, reply_markup=markup)  # ответ на сообщение
    bot.set_state(message.from_user.id, UserState.custom_user, message.chat.id)  # изменение статуса
